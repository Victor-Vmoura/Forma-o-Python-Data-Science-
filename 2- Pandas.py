# Importação da biblioteca pandas
import pandas as pd

# Carregamento do arquivo CSV
dados = pd.read_csv('aluguel.csv', sep=';')

# Visualização inicial dos dados
dados.head()

# Verificação do tipo do objeto 'dados'
type(dados)

# Exibição de informações gerais sobre o DataFrame
dados.info()

# Verificação dos tipos de dados de cada coluna
dados.dtypes

# Criação e exibição de um DataFrame com os tipos de dados
tipos_de_dados = pd.DataFrame(dados.dtypes, columns=['Tipos de Dados'])
tipos_de_dados.columns.name = 'Variáveis'
tipos_de_dados

# Verificação das dimensões (shape) do DataFrame
dados.shape

# Acessando o número de linhas e colunas
dados.shape[0]
dados.shape[1]

# Impressão do resumo da estrutura do DataFrame
print('A base de dados apresenta {} registros (imóveis) e {} variáveis'.format(dados.shape[0], dados.shape[1]))

# Análise e organização da variável 'Tipo'
dados['Tipo']

# Armazenando a Series 'Tipo' em uma variável
tipo_de_imovel = dados['Tipo']

# Verificando o tipo da nova variável
type(tipo_de_imovel)

# Removendo duplicatas (apenas para visualização)
tipo_de_imovel.drop_duplicates()

# Removendo duplicatas de forma permanente (inplace)
tipo_de_imovel.drop_duplicates(inplace=True)

# Visualizando a Series após a remoção de duplicatas
tipo_de_imovel

# Organizando a visualização da Series 'tipo_de_imovel'
tipo_de_imovel = pd.DataFrame(tipo_de_imovel)
tipo_de_imovel.index = range(tipo_de_imovel.shape[0])
tipo_de_imovel.columns.name = 'Id'
tipo_de_imovel

# Seleção de imóveis residenciais
dados.head()

# Criando uma lista de tipos de imóveis únicos
list(dados['Tipo'].drop_duplicates())

# Definindo a lista de tipos residenciais
residencial = ['Quitinete',
               'Casa',
               'Apartamento',
               'Casa de Condomínio',
               'Casa de Vila']
residencial

# Criando a máscara booleana para o filtro
selecao = dados['Tipo'].isin(residencial)
selecao

# Aplicando o filtro e criando o novo DataFrame
dados_residencial = dados[selecao]
dados_residencial

# Verificando os tipos de imóveis no novo DataFrame
list(dados_residencial['Tipo'].drop_duplicates())

# Verificando as dimensões do novo DataFrame
dados_residencial.shape[0]
dados.shape[0]

# Reorganizando o índice do DataFrame residencial
dados_residencial.index = range(dados_residencial.shape[0])
dados_residencial

# Exportando a base de dados para um arquivo CSV
dados_residencial.to_csv('aluguel_residencial.csv', sep=';')

# Lendo o arquivo salvo para verificar (com o índice antigo como coluna)
dados_residencial_2 = pd.read_csv('aluguel_residencial.csv', sep=';')
dados_residencial_2.head()

# Exportando novamente, desta vez sem o índice
dados_residencial.to_csv('aluguel_residencial.csv', sep=';', index=False)

# Lendo o arquivo final para verificação
dados_residencial_2 = pd.read_csv('aluguel_residencial.csv', sep=';')
dados_residencial_2.head()