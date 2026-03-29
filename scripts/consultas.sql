SELECT name FROM sqlite_master WHERE type='table';

SELECT * FROM tabela1 LIMIT 5;

SELECT COUNT(*) FROM tabela_analitica WHERE ISSN_Clean IS NULL;

-- Verificar a taxa de sucesso do Join (Quantos artigos ganharam dados internacionais)
SELECT 
    (COUNT(SJR) * 100.0 / COUNT(*)) as Percentual_Match
FROM tabela_analitica;

SELECT ISSN = 10009000
FROM tabela_analitica;