import pandas as pd
import plotly.express as px 

tabela = pd.read_csv('ClientesBanco.csv', encoding = 'Latin1')
tabela = tabela.drop('CLIENTNUM', axis=1)
tabela = tabela.dropna()
print(tabela.info())
print(tabela.describe())

qtd_categoria_perc = tabela['Categoria'].value_counts(normalize=True).round(2)
print(qtd_categoria_perc)

grafico = px.histogram(tabela, x='Idade', color='Categoria' )
grafico.show()