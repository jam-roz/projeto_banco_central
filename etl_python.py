import os
import requests
import pandas as pd
from datetime import datetime, timedelta
from dotenv import load_dotenv
from sqlalchemy import create_engine, text

#Carrega as senhas do arquivo .env
load_dotenv()
DATABASE_URL = os.getenv('DATABASE_URL')

def extrair_serie_historica(codigo_serie, nome_serie):
    """ Extrai a série do BCB com janela dinâmica segura. """
    hoje = datetime.today()
    data_final = hoje.strftime('%d/%m/%Y')
    
    #Reduzir para 3600 dias para dar uma folga maior ao limite de 10 anos do BCB
    data_inicial_dt = hoje - timedelta(days=3600)
    data_inicial = data_inicial_dt.strftime('%d/%m/%Y')
    
    url = f"https://api.bcb.gov.br/dados/serie/bcdata.sgs.{codigo_serie}/dados?formato=json&dataInicial={data_inicial}&dataFinal={data_final}"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        
        #Tratamento específico para o erro de JSON vazio do Banco Central
        try:
            dados_json = response.json()
        except ValueError:
            print(f"  -> Erro na API do BCB: O servidor retornou um valor vazio ou HTML inesperado em vez de JSON.")
            print(f"  -> Link para testar no navegador: {url}")
            return None
            
        df = pd.DataFrame(dados_json)
        
        #Limpeza
        df['data'] = pd.to_datetime(df['data'], format='%d/%m/%Y')
        df['valor'] = pd.to_numeric(df['valor'])
        df['serie_nome'] = nome_serie
        
        return df
    except requests.exceptions.RequestException as e:
        print(f"Erro ao conectar na série {nome_serie}: {e}")
        return None

def carregar_para_postgres(df, engine):
    """ Envia o DataFrame para o PostgreSQL de forma idempotente (sem duplicar). """
    #Renomeando as colunas do Pandas para ficarem iguais ao banco de dados
    df_banco = df.rename(columns={
        'data': 'data_referencia',
        'serie_nome': 'nome_serie'
    })
    
    
    df_banco.to_sql('temp_stage', engine, if_exists='replace', index=False)
    
    
    query_upsert = text("""
        INSERT INTO indicadores_macro (data_referencia, valor, nome_serie)
        SELECT data_referencia, valor, nome_serie FROM temp_stage
        ON CONFLICT (nome_serie, data_referencia) DO NOTHING;
    """)
    
    with engine.begin() as conn:
        conn.execute(query_upsert)
        conn.execute(text("DROP TABLE temp_stage;")) 

if __name__ == "__main__":
    print("Iniciando o Pipeline ETL (Extract, Transform, Load)...\n")
    
    #Criando a conexão com o banco de dados via SQLAlchemy
    engine = create_engine(DATABASE_URL)
    
    diretorio_script = os.path.dirname(os.path.abspath(__file__))
    pasta_data = os.path.join(diretorio_script, '..', 'data')
    os.makedirs(pasta_data, exist_ok=True)
    
    series_mapeadas = {
        'dolar_diario': 1,
        'ipca_mensal': 433,
        'selic_diaria': 11,
        'credito_mensal': 20632,
        'ibc_br_mensal': 1455
    }
    
    for nome, codigo in series_mapeadas.items():
        print(f"Extraindo: {nome} (Série {codigo})...")
        df_resultado = extrair_serie_historica(codigo_serie=codigo, nome_serie=nome)
        
        if df_resultado is not None and not df_resultado.empty:
            #Salvando na máquina (Backup em CSV)
            caminho_completo = os.path.join(pasta_data, f"stage_{nome}.csv")
            df_resultado.to_csv(caminho_completo, index=False)
            
            #Subindo para a Nuvem
            print(f"  -> Iniciando carga no PostgreSQL (Neon)...")
            carregar_para_postgres(df_resultado, engine)
            print(f"  -> Sucesso! {len(df_resultado)} registros processados.\n")
        else:
            print(f"  -> Falha ou dados vazios para a série {nome}.\n")
            
    print("Pipeline finalizado.")