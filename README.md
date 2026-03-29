# analise_prod_cientifica

## Como Executar o Projeto?
1. **Clone o repositório:**
   ```bash
   git clone -b dev [https://github.com/let-rocha/analise_prod_cientifica.git](https://github.com/let-rocha/analise_prod_cientifica.git)

OBS: Scripts estão na branc dev!!!

**Desafio Técnico: Análise de Qualidade e Impacto de Periódicos**
Este desafio é focado na análise de qualidade e impacto de 22 mil periódicos científicos entre 2019 e 2021.

Objetivos principais:
O objetivo principal é responder a perguntas estratégicas sobre a produção acadêmica:
- Qual a distribuição de qualidade (A1, A2, B1...) dos periódicos?
- Existe correlação real entre o prestígio (SJR) e o volume de citações?
- Como os periódicos brasileiros se comparam aos internacionais em termos de Quartil (Q1-Q4) e Índice H?

**Decisões técnicas e arquiteura:**

1. Saneamento e Cruzamento de Dados (ETL)
Desafio dos ISSNs: As bases originais apresentavam divergências de formatação. Foi implementada uma limpeza via Python para unificar os padrões e garantir um join entre a base QUALIS e os indicadores SCImago (SJR).

1.1. Normalização de Escala: Identificamos que o índice SJR estava em uma escala multiplicada (x1000). Apliquei uma transformação via DAX no Power BI para acertar a escala decimal correta (0.000), garantindo a precisão estatística.

2. Modelagem de Dados
Optei pelo SQLite pela portabilidade e performance em análises relacionais, permitindo que a tabela analítica final fosse consumida diretamente pelo Power BI via CSV.

3. Visualização Estratégica
O dashboard foi desenhado para responder perguntas de negócios relacionadas aos tais pontos abaixo:
- Identificação de periódicos Q1 (Top 5).
- Correlação entre prestígio e citações (Gráfico de dispersão).
- Distribuição regional (Drill-down geográfico).

**Stack Tecnológica**

    Python 3.11 (Pandas, Numpy, Sqlite3)

    SQLite (Armazenamento Relacional)

    Power BI (Business Intelligence & Storytelling)

    Git (Versionamento e Gestão de Branches)

**Arquitetura e Processo de ETL (Extract, Transform, Load)**

Estrutura do Repositório:
```text
├── data/               # Bases de dados originais e base tratada (CSVs)
 └── banco.db           # Banco de dados consolidado (SQLite)
├── scripts/
    └── etl_process.py  # Script Python automatizado de ETL         
    └── consultas.sql       # Script para consulta de dados 
├── requirements.txt    # Dependências do projeto
└── README.md           # Documentação do projeto
