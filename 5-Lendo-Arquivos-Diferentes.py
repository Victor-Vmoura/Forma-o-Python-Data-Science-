# Importação das bibliotecas necessárias
import pandas as pd
import json
import sqlite3

# --- Leitura de arquivos ---

# 1. Leitura de arquivo JSON
dados_json = pd.read_json('dados_medicos.json')
dados_json.head()

# 2. Leitura de arquivo JSON aninhado (normalizado)
with open('pacientes.json') as f:
    dados_pacientes = json.load(f)

dados_pacientes_normalizado = pd.json_normalize(dados_pacientes['pacientes'])
dados_pacientes_normalizado.head()

# 3. Leitura de arquivo JSON Lines (.jsonl)
dados_pacientes_2 = []
with open('pacientes_2.jsonl') as f:
    for linha in f:
        dados_pacientes_2.append(json.loads(linha))

df_pacientes_2 = pd.DataFrame(dados_pacientes_2)
df_pacientes_2.head()

# 4. Leitura de arquivo XML
dados_xml = pd.read_xml('dados_clinicos.xml')
dados_xml.head()

# 5. Interação com Banco de Dados (SQLite)
# Cria um banco de dados em memória
conexao = sqlite3.connect(':memory:')

# Escreve o DataFrame para uma tabela SQL
dados_xml.to_sql('pacientes', conexao, index=False)

# Define a query a ser executada
query = 'SELECT * FROM pacientes WHERE "Tipo_sanguineo" = "A-"'

# Lê o resultado da query para um novo DataFrame e o exibe
df_sql = pd.read_sql_query(query, conexao)
df_sql

# Fecha a conexão com o banco
conexao.close()

# 6. Leitura de arquivo Excel (.xlsx)
dados_excel = pd.read_excel('dados_imoveis.xlsx')
dados_excel.head()

# 7. Leitura de tabela HTML a partir de uma string
dados_html_string = """
<table>
  <thead>
    <tr>
      <th>Pais</th>
      <th>Capital</th>
      <th>Moeda</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Brasil</td>
      <td>Brasília</td>
      <td>Real</td>
    </tr>
    <tr>
      <td>Argentina</td>
      <td>Buenos Aires</td>
      <td>Peso</td>
    </tr>
     <tr>
      <td>Uruguai</td>
      <td>Montevidéu</td>
      <td>Peso</td>
    </tr>
  </tbody>
</table>
"""
dados_html = pd.read_html(dados_html_string)
dados_html_df = dados_html[0]
dados_html_df

# 8. Leitura de uma planilha do Google Sheets
sheet_id = '16_5_Y2k-2I5fM9o22f_1vzOalQ3cAbEp5eHe6x5yzh0'
url = f'https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet'
dados_gsheets = pd.read_csv(url)
dados_gsheets.head()