# --- Importação das bibliotecas ---
import pandas as pd
import plotly.express as px

# --- Carregamento e limpeza dos dados de emissões ---

# Carrega a planilha específica do arquivo Excel
emissoes_gases = pd.read_excel('/content/drive/MyDrive/Alura/dados/1-SEEG10_GERAL-BR_UF_2022.10.27-FINAL-SITE.xlsx', sheet_name = 'GEE Estados')

# Exibe o DataFrame carregado
emissoes_gases

# Exibe informações sobre o DataFrame
emissoes_gases.info()

# Mostra os valores únicos da coluna para entender os tipos de dados
emissoes_gases['Emissão / Remoção / Bunker'].unique()

# Cria uma máscara booleana para identificar linhas de remoção
(emissoes_gases['Emissão / Remoção / Bunker'] == 'Remoção NCI') | (emissoes_gases['Emissão / Remoção / Bunker'] == 'Remoção')

# Exibe as linhas que correspondem à remoção
emissoes_gases[emissoes_gases['Emissão / Remoção / Bunker'].isin(['Remoção NCI', 'Remoção'])]

# Exibe os valores de emissão para as linhas de remoção ao longo dos anos
emissoes_gases.loc[emissoes_gases['Emissão / Remoção / Bunker'].isin(['Remoção NCI', 'Remoção']), 1970:2021]

# Verifica o valor máximo para as linhas de remoção (para confirmar se são todos negativos ou zero)
emissoes_gases.loc[emissoes_gases['Emissão / Remoção / Bunker'].isin(['Remoção NCI', 'Remoção']), 1970:2021].max()

# Verifica os estados associados ao tipo 'Bunker'
emissoes_gases.loc[emissoes_gases['Emissão / Remoção / Bunker'] == 'Bunker', 'Estado'].unique()

# Filtra o DataFrame para manter apenas as linhas de 'Emissão' e o exibe
emissoes_gases = emissoes_gases[emissoes_gases['Emissão / Remoção / Bunker'] == 'Emissão']
emissoes_gases

# Remove a coluna 'Emissão / Remoção / Bunker' e exibe o DataFrame resultante
emissoes_gases = emissoes_gases.drop(columns = 'Emissão / Remoção / Bunker')
emissoes_gases

# --- Reestruturação do DataFrame (melt) ---

# Define as colunas que não são de anos (identificadoras)
colunas_info = list(emissoes_gases.loc[:,'Nível 1 - Setor':'Produto'].columns)
colunas_info

# Define as colunas que representam os anos (valores)
colunas_emissao = list(emissoes_gases.loc[:,1970:2021].columns)
colunas_emissao

# Transforma as colunas de anos em uma única coluna 'Ano' e seus valores em 'Emissão'
emissoes_por_ano = emissoes_gases.melt(id_vars = colunas_info, value_vars = colunas_emissao, var_name = 'Ano' , value_name = 'Emissão')
emissoes_por_ano

# --- Análise e agrupamento ---

# Agrupa os dados por Gás
emissoes_por_ano.groupby('Gás').groups
emissoes_por_ano.groupby('Gás').get_group('CO2 (t)')
emissoes_por_ano.groupby('Gás').sum(numeric_only=True)

# Agrupa as emissões totais por tipo de gás e ordena
emissao_por_gas = emissoes_por_ano.groupby('Gás').sum(numeric_only=True).sort_values('Emissão', ascending = False)
emissao_por_gas

# Gera o gráfico de barras da emissão total por tipo de gás
emissao_por_gas.plot(kind = 'barh', figsize = (10,6));

# Exibe as 9 maiores fontes de emissão
emissao_por_gas.iloc[0:9]

# Calcula e imprime o percentual de emissão de CO2 em relação ao total
print(f'A emissão de CO2 corresponde a {float(emissao_por_gas.iloc[0:9].sum()/emissao_por_gas.sum())*100:.2f} % de emissão total de gases estufa no Brasil de 1970 a 2021.')

# Agrupa as emissões por gás e por setor
gas_por_setor = emissoes_por_ano.groupby(['Gás', 'Nível 1 - Setor']).sum(numeric_only=True)
gas_por_setor

# Extrai os dados apenas para o gás CO2
gas_por_setor.xs('CO2 (t)', level = 0)

# Extrai um valor específico (cruzamento de gás e setor)
gas_por_setor.xs(('CO2 (t)', 'Mudança de Uso da Terra e Floresta'), level = [0,1])

# Encontra o valor máximo de emissão para o gás CO2
gas_por_setor.xs('CO2 (t)', level = 0).max()

# Encontra o setor com a maior emissão de CO2
gas_por_setor.xs('CO2 (t)', level = 0).idxmax()

# Encontra o setor de maior emissão para cada tipo de gás
gas_por_setor.groupby(level = 0).idxmax()

# Cria uma tabela sumarizada para encontrar o setor de maior emissão para cada gás
valores_max = gas_por_setor.groupby(level = 0).max().values
tabela_sumarizada = gas_por_setor.groupby(level = 0).idxmax()
tabela_sumarizada.insert(1, 'Quantidade de emissão', valores_max)
tabela_sumarizada

# Inverte os níveis do índice para encontrar o gás mais emitido por setor
gas_por_setor.swaplevel(0, 1)
gas_por_setor.swaplevel(0, 1).groupby(level = 0).idxmax()

# Gráfico da média de emissões ao longo dos anos
emissoes_por_ano.groupby('Ano').mean(numeric_only=True).plot(figsize = (10,6));

# Encontra o ano com a maior média de emissão
emissoes_por_ano.groupby('Ano').mean(numeric_only=True).idxmax()

# Agrupa a média de emissões por ano e por gás
media_emissao_anual = emissoes_por_ano.groupby(['Ano', 'Gás']).mean(numeric_only=True).reset_index()
media_emissao_anual

# Pivota a tabela para ter anos como índice e gases como colunas e a exibe
media_emissao_anual = media_emissao_anual.pivot_table(index = 'Ano', columns = 'Gás', values = 'Emissão')
media_emissao_anual

# Gera gráficos de linha para a emissão de cada gás ao longo do tempo
media_emissao_anual.plot(subplots = True, figsize = (10,40));

# --- Carregamento e limpeza dos dados de população ---

# Carrega os dados de população, pulando cabeçalho e rodapé desnecessários
populacao_estados = pd.read_excel('/content/drive/MyDrive/Alura/dados/POP2022_Municipios.xls', header = 1, skipfooter = 34)
populacao_estados

# Exibe o agrupamento inicial que não funciona como esperado
populacao_estados.groupby('UF').sum(numeric_only=True)

# Exibe as linhas com caracteres não numéricos na coluna de população
populacao_estados[populacao_estados['POPULAÇÃO'].str.contains('\\(', na = False)]

# Limpa a coluna de população, removendo caracteres especiais e pontos
populacao_estados = populacao_estados.assign(populacao_sem_parenteses = populacao_estados['POPULAÇÃO'].replace('\\(\\d{1,2}\\)', '', regex = True),
                                             populacao = lambda x: x.loc[:,'populacao_sem_parenteses'].replace('\\.', '', regex = True))

# Exibe novamente as linhas que foram tratadas para verificação
populacao_estados[populacao_estados['POPULAÇÃO'].str.contains('\\(', na = False)]

# Converte a nova coluna de população para o tipo inteiro
populacao_estados.loc[:,'populacao'] = populacao_estados['populacao'].astype(int)

# Agrupa os dados por estado (UF) para obter a população total e exibe
populacao_estados = populacao_estados.groupby('UF').sum(numeric_only=True)['populacao'].reset_index()
populacao_estados

# --- Junção dos dados e cálculo per capita ---

# Filtra os dados de emissão para o ano de 2021 e agrupa por estado
emissao_estados = emissoes_por_ano[emissoes_por_ano['Ano'] == 2021].groupby('Estado').sum(numeric_only=True).reset_index()
emissao_estados

# Junta os DataFrames de emissão e população e exibe o resultado
dados_agrupados = pd.merge(emissao_estados, populacao_estados, left_on = 'Estado', right_on = 'UF')
dados_agrupados

# Calcula a emissão per capita e ordena os estados, exibindo o resultado final
dados_agrupados = dados_agrupados.assign(emissao_per_capita = dados_agrupados['Emissão']/dados_agrupados['populacao']).sort_values('emissao_per_capita', ascending = False)
dados_agrupados

# --- Visualizações Finais ---

# Gráfico de dispersão: População vs. Emissão
dados_agrupados.plot(x = 'populacao', y= 'Emissão', kind = 'scatter', figsize=(8,6));

# Gráfico de dispersão interativo com texto
px.scatter(data_frame = dados_agrupados, x = 'populacao', y = 'Emissão', text = 'Estado', opacity = 0)

# Gráfico de barras da emissão per capita por estado
px.bar(data_frame = dados_agrupados, x = 'Estado', y = 'emissao_per_capita')

# Gráfico de dispersão interativo com tamanho dos pontos representando a emissão per capita
px.scatter(data_frame = dados_agrupados, x = 'populacao', y = 'Emissão', text = 'Estado', size = 'emissao_per_capita')
