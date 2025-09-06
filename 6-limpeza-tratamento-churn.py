import pandas as pd

# Carregamento do arquivo JSON e visualização inicial
dados_churn = pd.read_json('customer_churn.json')
dados_churn.head()

# Mostra uma forma alternativa de carregar os dados
pd.read_json('customer_churn.json', orient='records')

# Exibe informações gerais sobre o DataFrame
dados_churn.info()

# Exibição de colunas específicas para inspeção
dados_churn['customerID']
dados_churn.customerID
dados_churn['Churn']

# Identifica e filtra linhas com valores problemáticos na coluna 'Churn'
dados_churn.query("Churn == ''")
dados_churn.query("Churn != ''")
dados_churn = dados_churn.query("Churn != ''")

# Verifica as informações do DataFrame após a primeira limpeza
dados_churn.info()

# Exibe a coluna 'TotalCharges'
dados_churn.TotalCharges

# Identifica e filtra linhas com valores problemáticos na coluna 'TotalCharges'
dados_churn.query("TotalCharges == ' '")
dados_churn.query("TotalCharges != ' '")
dados_churn = dados_churn[dados_churn['TotalCharges'] != ' ']

# Verifica as informações após a segunda limpeza
dados_churn.info()

# Converte a coluna 'TotalCharges' para o tipo numérico
dados_churn.TotalCharges = pd.to_numeric(dados_churn.TotalCharges)

# Verifica as informações após a conversão de tipo
dados_churn.info()

# Verificação dos valores únicos nas colunas categóricas
dados_churn.gender.unique()
dados_churn.Partner.unique()
dados_churn.Dependents.unique()
dados_churn.PhoneService.unique()
dados_churn.MultipleLines.unique()
dados_churn.OnlineSecurity.unique()
dados_churn.OnlineBackup.unique()
dados_churn.DeviceProtection.unique()
dados_churn.TechSupport.unique()
dados_churn.StreamingTV.unique()
dados_churn.StreamingMovies.unique()
dados_churn.Contract.unique()
dados_churn.PaperlessBilling.unique()
dados_churn.PaymentMethod.unique()
dados_churn.Churn.unique()

# Transformação de dados (Mapeamento)
# Substitui 'No' por 0 e 'Yes' por 1
dados_churn.replace(to_replace='No', value=0, inplace=True)
dados_churn.replace(to_replace='Yes', value=1, inplace=True)

# Define um dicionário para substituir valores específicos
dicionario = {'No phone service': 0, 'No internet service': 0}
dados_churn = dados_churn.replace(dicionario)

# Substitui os valores da coluna 'gender'
dados_churn.gender.replace(['Male', 'Female'], [0, 1], inplace=True)

# Visualiza o DataFrame após as substituições
dados_churn.head()

# Transformação de dados (One-Hot Encoding / Dummification)
# Cria variáveis dummy para as colunas categóricas restantes
dados_churn_sem_categorico = pd.get_dummies(dados_churn).copy()

# Exibe o DataFrame final
dados_churn_sem_categorico.head()

# Verifica as informações e o formato do DataFrame final
dados_churn_sem_categorico.info()
dados_churn_sem_categorico.shape