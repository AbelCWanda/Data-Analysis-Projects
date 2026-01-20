🧹 Data Cleaning Project: De Dados Brutos a Dados Prontos para Análise
🎯 Objetivo do Projeto
Este projeto demonstra o processo de limpeza e transformação de uma base de dados de clientes (originalmente desorganizada) utilizando o Microsoft Excel. O objetivo foi transformar dados "sujos" e inconsistentes em um conjunto de dados estruturado e confiável para análises futuras.


🛠️ O que foi feito? (Processo de Limpeza)
Analisei o arquivo Raw Data e apliquei as seguintes correções para chegar ao arquivo Cleaned Data:

1. Padronização de Nomes: Removi espaços desnecessários no início e no fim dos nomes (utilizando a função ARRUMAR ou TRIM).
2. Correção de Tipos de Dados: Converti idades que estavam em formato de texto (ex: "twenty") para o formato numérico (20).
3. Tratei valores ausentes na coluna Age utilizando a média aritmética (30.19).
4. Normalização de Gênero e Estado Civil: Padronizei entradas inconsistentes como "M", "Male" para "Male", e corrigi erros de digitação (ex: "Sungle" para "Single", "Marrd" para "Marred").
5. Tratamento de Datas: Corrigi formatos de datas inconsistentes para o padrão DD/MM/AAAA.
6. Tratamento de Localização: Preenchi valores nulos (N/A) na coluna de localização e padronizei nomes de cidades/países.
6. Auditoria de Dados: Criei uma coluna Count_blanck para identificar e monitorar linhas que ainda possuíam informações em falta durante o processo.

📁 Estrutura dos Arquivos
1. Raw Data: Os dados originais com erros de digitação, espaços extras, formatos de data inconsistentes e valores nulos.
2. Cleaned Data: A versão final, limpa, padronizada e pronta para ser importada para ferramentas como Power BI ou SQL

💡 Competências Demonstradas
1. Manipulação de Strings (Nomes e Textos).
2. Tratamento de Outliers e Valores Nulos.
3. Conhecimento em Funções Lógicas e de Pesquisa no Excel.
4. Preparação de Dados para ETL (Extract, Transform, Load).


🚀 Como visualizar
Basta baixar o arquivo .xlsx deste repositório e alternar entre as abas para comparar o estado inicial e final dos dados.
