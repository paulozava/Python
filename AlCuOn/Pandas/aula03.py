import pandas as pd

dados = pandas.read_csv('/home/laumzav/PycharmProjects/Python_study/AlCuOn/Pandas/aluguel.csv', sep=';')
dados.head(10)
dados.dtypes