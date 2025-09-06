import numpy as np
import matplotlib.pyplot as plt

# Define a URL dos dados
url = 'https://raw.githubusercontent.com/alura-cursos/numpy/dados/apples_ts.csv'

# Gera um array de 1 a 87 para usar no 'usecols'
np.arange(1, 88, 1)

# Calcula o número de colunas (7 anos * 12 meses + 3 meses)
7*12+3

# Carrega os dados do arquivo, pulando a primeira coluna
dado = np.loadtxt(url, delimiter=',', usecols=np.arange(1, 88, 1))

# Verifica a dimensionalidade do array
dado.ndim

# Verifica o número total de elementos
dado.size

# Verifica o formato (shape) do array
dado.shape

# Transpõe a matriz de dados e a exibe
dado.T

# Verifica o novo formato após a transposição
dado.T.shape

# Armazena a matriz transposta em uma nova variável
dado_transposto = dado.T

# Separa as datas e os preços
datas = dado_transposto[:, 0]
precos = dado_transposto[:, 1:6]

# Plota o gráfico de preços da primeira cidade (Moscow)
plt.plot(datas, precos[:, 0])

# Cria um novo array de datas para usar como eixo X
datas = np.arange(1, 88, 1)

# Plota o gráfico novamente com o novo eixo X
plt.plot(datas, precos[:, 0])

# Define os arrays para cada cidade
Moscow = precos[:, 0]
Kaliningrad = precos[:, 1]
Petersburg = precos[:, 2]
Krasnodar = precos[:, 3]
Ekaterinburg = precos[:, 4]

# Verifica o formato do array de Moscou
Moscow.shape

# Fatiamento dos dados de Moscou por ano
Moscow_ano1 = Moscow[0:12]
Moscow_ano2 = Moscow[12:24]
Moscow_ano3 = Moscow[24:36]
Moscow_ano4 = Moscow[36:48]

# Plota os preços de cada ano para Moscou
plt.plot(np.arange(1, 13, 1), Moscow_ano1)
plt.plot(np.arange(1, 13, 1), Moscow_ano2)
plt.plot(np.arange(1, 13, 1), Moscow_ano3)
plt.plot(np.arange(1, 13, 1), Moscow_ano4)
plt.legend(['ano1', 'ano2', 'ano3', 'ano4'])

# Compara se os arrays dos anos 3 e 4 são exatamente iguais
np.array_equal(Moscow_ano3, Moscow_ano4)

# Compara se os arrays são próximos, com uma tolerância de 10
np.allclose(Moscow_ano3, Moscow_ano4, 10)

# Plota o gráfico de preços de Kaliningrad, mostrando a descontinuidade do NaN
plt.plot(datas, Kaliningrad)

# Verifica quais elementos do array de Kaliningrad são NaN (Not a Number)
np.isnan(Kaliningrad)

# Exibe o array de Kaliningrad
Kaliningrad

# Soma a quantidade de valores NaN no array
sum(np.isnan(Kaliningrad))

# Calcula a média entre os valores adjacentes ao NaN (índices 3 e 5)
(Kaliningrad[3] + Kaliningrad[5]) / 2
np.mean([Kaliningrad[3], Kaliningrad[5]])

# Substitui o valor NaN pela média calculada
Kaliningrad[4] = np.mean([Kaliningrad[3], Kaliningrad[5]])

# Calcula a média de preços de Moscou e Kaliningrad
np.mean(Moscow)
np.mean(Kaliningrad)

# Regressão linear simples
# Define as variáveis para o ajuste da reta
x = datas
y = 2 * x + 80

# Plota o gráfico de preços de Moscou e a reta de exemplo
plt.plot(datas, Moscow)
plt.plot(datas, y)

# Calcula a norma (distância euclidiana) entre os preços reais e a reta de exemplo
np.sqrt(np.sum(np.power(Moscow - y, 2)))

# Define uma nova reta com coeficientes diferentes
y = 0.52 * x + 80

# Plota novamente para comparação
plt.plot(datas, Moscow)
plt.plot(datas, y)

# Mostra a diferença elemento a elemento
Moscow - y

# Calcula a nova norma do erro
np.sqrt(np.sum(np.power(Moscow - y, 2)))
np.linalg.norm(Moscow - y)

# Cálculo dos coeficientes da regressão linear
Y = Moscow
X = datas
n = np.size(Moscow)

X.shape
(X**2).shape

# Calcula o coeficiente angular 'a'
a = (n * np.sum(X * Y) - np.sum(X) * np.sum(Y)) / (n * np.sum(X**2) - np.sum(X)**2)

# Calcula o coeficiente linear 'b'
b = np.mean(Y) - a * np.mean(X)

# Gera a linha da regressão
y = a * X + b

# Calcula a norma do erro com os coeficientes otimizados
np.linalg.norm(Moscow - y)

# Plota os dados originais, a linha de regressão e a projeção para o futuro
plt.plot(datas, Moscow)
plt.plot(datas, y)
plt.plot(41.5, a * 41.5 + b, '*r')
plt.plot(100, a * 100 + b, '*r')

# Geração de números aleatórios
np.random.randint(low=40, high=100, size=100)
coef_angulares = np.random.uniform(low=0.10, high=0.90, size=100)

# Exibe o coeficiente linear 'b'
b

# Loop para calcular a norma do erro para 100 coeficientes angulares aleatórios
norma = np.array([])
for i in range(100):
    norma = np.append(norma, np.linalg.norm(Moscow - (coef_angulares[i] * X + b)))

# Exibe o array de normas
norma

# Exibe o coeficiente angular na posição 3
coef_angulares[3]

# Demonstração da reprodutibilidade com np.random.seed
np.random.uniform(low=0.10, high=0.90, size=100)
np.random.seed(16)
np.random.uniform(low=0.10, high=0.90, size=100)

# Recalcula a norma usando uma semente para reprodutibilidade
norma = np.array([])
np.random.seed(84)
coef_angulares = np.random.uniform(low=0.10, high=0.90, size=100)

for i in range(100):
    norma = np.append(norma, np.linalg.norm(Moscow - (coef_angulares[i] * X + b)))

# Combina a norma e os coeficientes em um único array
dados = np.column_stack([norma, coef_angulares])

# Verifica o formato do novo array
dados.shape

# Salva o array resultante em um arquivo CSV
np.savetxt('dados.csv', dados, delimiter=',')
