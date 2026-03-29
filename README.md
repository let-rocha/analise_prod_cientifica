# analise_prod_cientifica
Desafio Técnico: Análise de Qualidade e Impacto de Periódicos
Objetivos principais:
O objetivo principal é responder a perguntas estratégicas sobre a produção acadêmica:
- Qual a distribuição de qualidade (A1, A2, B1...) dos periódicos?
- Existe correlação real entre o prestígio (SJR) e o volume de citações?
- Como os periódicos brasileiros se comparam aos internacionais em termos de Quartil (Q1-Q4) e Índice H?

Stack Tecnológica:
- **Linguagem:** Python 3.12
- **Bibliotecas de Dados:** Pandas (ETL e Limpeza)
- **Banco de Dados:** SQLite (Armazenamento e Modelagem)
- **Visualização:** Power BI
- **IDE:** VS Code

Arquitetura e Processo de ETL (Extract, Transform, Load)

Estrutura do Repositório:
```text
├── data/               # Bases de dados originais e base tratada (CSVs)
 └── banco.db           # Banco de dados consolidado (SQLite)
├── scripts/
    └── etl_process.py  # Script Python automatizado de ETL         
    └── consultas.sql       # Script para consulta de dados 
├── requirements.txt    # Dependências do projeto
└── README.md           # Documentação do projeto

