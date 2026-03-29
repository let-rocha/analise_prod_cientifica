import sqlite3
import pandas as pd

# --- ETAPA DE EXTRAÇÃO ---
# 1. Conectando no banco (Abre uma única vez)
conn = sqlite3.connect('banco.db')

# Carregando os CSVs
artigos_1 = pd.read_csv(r'C:\Users\letic\Desktop\Datasets_Desafio_Tecnico_AS\meu-projeto-qualis\meu-projeto-qualis\data\artigos_fi1.csv')
artigos_2 = pd.read_csv(r'C:\Users\letic\Desktop\Datasets_Desafio_Tecnico_AS\meu-projeto-qualis\meu-projeto-qualis\data\artigos_fi2.csv')

# Enviando para o SQLite as tabelas brutas
artigos_1.to_sql('tabela1', conn, if_exists='replace', index=False)
artigos_2.to_sql('tabela2', conn, if_exists='replace', index=False)

print("Dados brutos carregados com sucesso!")

# Lendo os dados do SQLite (usando a conexão que já está aberta)
df1 = pd.read_sql("SELECT * FROM tabela1", conn)
df2 = pd.read_sql("SELECT * FROM tabela2", conn)

# --- ETAPA DE TRANSFORMAÇÃO ---

def converter_decimal(texto):
    if pd.isna(texto) or texto == '0' or texto == '-': 
        return 0.0
    if isinstance(texto, str):
        texto = texto.replace(',', '.')
    try:
        return float(texto)
    except:
        return 0.0

# Tratamento tabela 1
df1['ISSN_Clean'] = df1['ISSN'].astype(str).str.replace('-', '').str.strip()
df1['FI (SJR)'] = df1['FI (SJR)'].apply(converter_decimal)

# Tratamento tabela 2
df2['Issn_List'] = df2['Issn'].astype(str).str.split(',') # .astype(str) garante que nulos não quebrem o split
df2_exploded = df2.explode('Issn_List')
df2_exploded['ISSN_Clean'] = df2_exploded['Issn_List'].str.replace('-', '').str.strip()
df2_exploded['SJR'] = df2_exploded['SJR'].apply(converter_decimal)
df2_exploded['Cites / Doc. (2years)'] = df2_exploded['Cites / Doc. (2years)'].apply(converter_decimal)

# Unificação de tabelas 1 e 2 (JOIN)
colunas_scimago = ['ISSN_Clean', 'SJR', 'SJR Best Quartile', 'Country', 'Region', 'Categories']

df_final = pd.merge(
    df1, 
    df2_exploded[colunas_scimago], 
    on='ISSN_Clean', 
    how='left'
)

# Limpeza de duplicatas e nulos
df_final = df_final.drop_duplicates(subset=['ISSN', 'PERIÓDICO', 'QUALIS'])
df_final['SJR Best Quartile'] = df_final['SJR Best Quartile'].fillna('Não Classificado')
df_final['Country'] = df_final['Country'].fillna('Não Informado')
df_final['Region'] = df_final['Region'].fillna('Não Informado')

# --- ETAPA DE CARREGAMENTO ---
# Salvando a tabela final
df_final.to_sql('tabela_analitica', conn, if_exists='replace', index=False)

# Fechando a conexão
conn.close()

print("ETL finalizado com sucesso! Tabela 'tabela_analitica' criada.")
print(f"Colunas finais: {df_final.columns.tolist()}")

# Gerando um CSV da tabela final (tabel_analitica) para fazer a visualização
df_final.to_csv('data/tabela_analitica.csv', index=False, sep=';', encoding='utf-8-sig')