# 📈 Pipeline de Dados: Indicadores Econômicos (Banco Central do Brasil)

![Power BI](https://img.shields.io/badge/Power_BI-F2C811?style=for-the-badge&logo=powerbi&logoColor=black)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)

> **Resumo:** Este projeto é um pipeline de Engenharia de Dados automatizado, desenvolvido para extrair, tratar e persistir indicadores macroeconômicos da API do Banco Central do Brasil (BCB). A solução elimina a coleta manual de dados, garantindo um banco de dados atualizado diariamente para suporte a dashboards de Business Intelligence.

## 🎥 Preview do Dashboard

https://github.com/user-attachments/assets/d1ac2a6c-42d3-466b-8a5d-ded0e0980d18

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

## 📊 Resultados e Insights Analíticos
* ### 1. O "Efeito Tesoura" nas Margens (Dólar vs. IPCA)

- **O Cenário:** Foi identificada uma assimetria entre o custo de aquisição e o custo de vida. No período analisado (Jan - Atual), o Dólar apresentou uma retração de 5% (caindo de R$ 5,44 para R$ 5,17), enquanto a inflação (IPCA) acelerou em 0,34 p.p. (de 0,33% para 0,67%).
- **Impacto Operacional:** O custo de reposição de mercadorias importadas ou com insumos dolarizados ficou mais barato, enquanto o mercado interno sofre pressão inflacionária.
- **Ação Recomendada:** Manutenção do preço final de venda para absorção de uma maior margem de lucro (Markup). Evitar o repasse da queda do dólar ao consumidor final permite um ganho de rentabilidade invisível frente à concorrência, que precisará reajustar preços devido à inflação interna.

### 2. Estagnação de Demanda e Custo de Capital (Selic vs. Crédito PJ)

- **O Cenário:** A taxa Selic manteve-se em patamares contracionistas (oscilando entre 14,15% e 14,90%). Ao analisar o Volume de Crédito (PJ) na visão Year-over-Year (YoY), houve um avanço nominal de R$ 295 Bi para R$ 314 Bi (crescimento de ~6,4%).
- **Impacto Operacional:** Considerando a inflação do período, o crescimento real do crédito foi virtualmente nulo. O mercado não está em expansão, e o alto custo do dinheiro encarece as taxas de antecipação de recebíveis em plataformas de marketplace.
- **Ação Recomendada:** * Foco absoluto em produtos "Curva A" (giro rápido) para evitar custo de capital parado em estoque.
    - Estruturação de campanhas de incentivo para pagamentos à vista (PIX/Boleto), mitigando a corrosão do fluxo de caixa pelas taxas de antecipação de cartão de crédito.
    - Esforços direcionados para retenção de clientes (aumento de LTV), dado que a captação de novos clientes em um mercado de crédito estagnado é mais custosa (CAC elevado).

## 📎 Créditos e Atribuições
* **Fonte de Dados:** API do Banco Central do Brasil (SGS - Sistema Gerenciador de Séries Temporais).
