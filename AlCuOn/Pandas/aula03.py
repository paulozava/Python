import pandas as pd

dados = pd.read_csv('/home/laumzav/PycharmProjects/Python_study/AlCuOn/Pandas/aluguel.csv', sep=';')
dados.head(10)
dados.dtypes
tipos = list(dados['Tipo'].drop_duplicates())
residencial = ['Quitinete', 'Casa', 'Apartamento', 'Casa de Condomínio', 'Flat', 'Casa de Vila', 'Loft']
dados['Residencial'] = dados['Tipo'].isin(residencial)