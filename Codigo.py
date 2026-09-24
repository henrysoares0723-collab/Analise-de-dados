import pandas as pd

tabela = pd.read_csv('ClientesBanco.csv', encoding = 'Latin1')
tabela = tabela.drop('CLIENTNUM', axis=1)
print(tabela)