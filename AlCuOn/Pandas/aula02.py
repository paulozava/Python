import pandas
import pandas as pd

dados = pandas.read_csv('/home/laumzav/PycharmProjects/Python_study/AlCuOn/Pandas/aluguel.csv', sep=';')
dados.head(10)
dados.dtypes

tipos_imoveis = dados['Tipo']
tipos_imoveis.drop_duplicates(inplace=True)
tipos_imoveis

dados.drop(columns=['Valor', 'Condominio', 'IPTU'], inplace=True)
dados.dtypes
dados


df1 = pandas.DataFrame({'A': {'X': 1}, 'B': {'X': 2}})
df2 = pandas.DataFrame({'C': {'X': 3}, 'D': {'X': 4}})
pandas.concat([df1, df2])

dados = [('A', 'B'), ('C', 'D')]
df = pd.DataFrame(dados, columns = ['L1', 'L2'],  index = ['C1', 'C2'])
df

dados = [[1, 2, 3], [4, 5, 6]]
index = 'X,Y'.split(',')
columns = list('CBA')[::-1]
df = pd.DataFrame(dados, index, columns)
df

dados = {'A': {'X': 1, 'Y': 3}, 'B': {'X': 2, 'Y': 4}}
df = pd.DataFrame(dados)
df