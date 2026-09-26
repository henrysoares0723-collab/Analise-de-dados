import pandas as pd
import plotly.express as px 

tabela = pd.read_csv('ClientesBanco.csv', encoding = 'Latin1')
tabela = tabela.drop('CLIENTNUM', axis=1)
tabela = tabela.dropna()
print(tabela.info())
print(tabela.describe())

qtd_categoria_perc = tabela['Categoria'].value_counts(normalize=True).round(2)
print(qtd_categoria_perc)

for coluna in tabela:
    grafico = px.histogram(tabela, x=coluna, color='Categoria' )
    grafico.show()

#De acordo com analise dos graficos noata-se que quanto mia sprodutos contratados um cliente tem, menor a chance dele cancelar, e quanto mais transações e maior o vsalor de transações, menor a chance de cancelar
#Quanto maior a quantidade de contatos que a pessoa teve que fazer, maior a chance de ser cancelado 