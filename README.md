# 📈 Pipeline de Dados: Indicadores Econômicos (Banco Central do Brasil)

![Power BI](https://img.shields.io/badge/Power_BI-F2C811?style=for-the-badge&logo=powerbi&logoColor=black)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)

> **Resumo:** Este projeto é um pipeline de Engenharia de Dados automatizado, desenvolvido para extrair, tratar e persistir indicadores macroeconômicos da API do Banco Central do Brasil (BCB). A solução elimina a coleta manual de dados, garantindo um banco de dados atualizado diariamente para suporte a dashboards de Business Intelligence.

## 🎥 Preview do Dashboard
*(Insira aqui o link ou GIF do seu Dashboard no Power BI)*

## 📌 O Problema de Negócio
A análise de indicadores econômicos (como Dólar, IPCA e Selic) exige dados precisos e atualizados. A coleta manual em sites de órgãos públicos é uma tarefa repetitiva, propensa a erros e ineficiente para análises temporais longas. Este projeto soluciona essa defasagem criando um fluxo de dados resiliente (ETL) que garante que o dashboard de BI esteja sempre refletindo a realidade econômica atual sem intervenção humana.

## 🛠️ Stack Tecnológica e Arquitetura
O projeto foi construído sobre uma arquitetura de nuvem e automação:

1. **Python (Requests/Pandas):** Extração via API do BCB e tratamento de séries temporais.
2. **PostgreSQL (SQLAlchemy):** Armazenamento estruturado e persistência dos dados.
3. **GitHub Actions:** Automação de workflow CI/CD que executa o pipeline diariamente às 06:00 (UTC).
4. **Power BI:** Conexão direta com o banco de dados para visualização dinâmica.

## 🗄️ Tratamento de Dados (ETL) e Regras de Negócio
* **Conectividade Dinâmica:** Extração automatizada com janelas de data móveis para garantir o histórico completo.
* **Tratamento de Exceções:** Implementação de camadas de segurança para lidar com falhas na API do BCB e dados vazios.
* **Persistência Segura:** Uso de variáveis de ambiente e *GitHub Secrets* para proteger credenciais de banco de dados em produção.
* **Automação (CI/CD):** O GitHub Actions orquestra a execução, gerencia as dependências (`requirements.txt`) e garante a integridade dos dados no servidor.

## 💡 Principais Funcionalidades
* **Atualização Zero-Touch:** O pipeline roda de forma autônoma, puxando todos os dados estratégicos automaticamente.
* **Segurança por Design:** Credenciais de banco de dados isoladas do código-fonte através do gerenciamento de segredos do GitHub.
* **Escalabilidade:** Estrutura pronta para inclusão de novas séries temporais do BCB apenas adicionando o código da série ao mapeamento do script.

## 📊 Principais Insights de Negócio
* **Correlação de Indicadores:** O dashboard permite visualizar a correlação direta entre a variação da Taxa Selic e o comportamento do Dólar ao longo do tempo.
* **Volatilidade Econômica:** A visualização de séries temporais longas permite identificar picos de volatilidade causados por eventos macroeconômicos específicos.
* **Qualidade da Informação:** A automatização remove o viés de erros de digitação humanos que ocorriam anteriormente na coleta manual.

## 📎 Créditos e Atribuições
* **Fonte de Dados:** API do Banco Central do Brasil (SGS - Sistema Gerenciador de Séries Temporais).
