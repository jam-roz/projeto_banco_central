--Criação da tabela principal
CREATE TABLE IF NOT EXISTS indicadores_macro (
    data_referencia DATE NOT NULL,
    valor NUMERIC NOT NULL,
    nome_serie VARCHAR(50) NOT NULL,
    
    -- Criamos uma Chave Primária Composta para evitar duplicações no futuro
    PRIMARY KEY (nome_serie, data_referencia)
);

--Dólar e Selic (Tabela Fato Diária)
CREATE OR REPLACE VIEW vw_fato_diaria AS
SELECT 
    data_referencia AS data_exata,
    MAX(CASE WHEN nome_serie = 'dolar_diario' THEN valor END) AS dolar,
    MAX(CASE WHEN nome_serie = 'selic_diaria' THEN (valor / 100.0) END) AS selic
FROM indicadores_macro
WHERE nome_serie IN ('dolar_diario', 'selic_diaria')
GROUP BY data_referencia
ORDER BY data_exata;

--IPCA, Crédito, IBC-Br (Tabela Fato Mensal)
CREATE OR REPLACE VIEW vw_fato_mensal AS
SELECT 
    DATE_TRUNC('month', data_referencia)::DATE AS mes_ano,
    MAX(CASE WHEN nome_serie = 'ipca_mensal' THEN (valor / 100.0) END) AS ipca,
    MAX(CASE WHEN nome_serie = 'credito_mensal' THEN valor END) AS credito,
    MAX(CASE WHEN nome_serie = 'ibc_br_mensal' THEN valor END) AS ibc_br
FROM indicadores_macro
WHERE nome_serie IN ('ipca_mensal', 'credito_mensal', 'ibc_br_mensal')
GROUP BY DATE_TRUNC('month', data_referencia)::DATE
ORDER BY mes_ano;
