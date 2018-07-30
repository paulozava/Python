import pandas as pd

alugueis = pd.read_csv('/home/laumzav/PycharmProjects/Python_study/AlCuOn/Pandas/aluguel.csv', sep=';')
# alugueis.info()
# alugueis['Valor'].isna()
alugueis.dropna(subset=['Valor'], inplace=True)
# alugueis.info()
# alugueis[['Tipo','Condominio']]


# alugueis.info()
# selection = list((alugueis['Tipo'] == 'Apartamento') & (alugueis['Condominio'].isna()))
# selection = [not b for b in selection]
# alugueis = alugueis[selection]

selection = (alugueis['Tipo'] == 'Apartamento') & (alugueis['Condominio'].isna())
alugueis = alugueis[~selection]
alugueis['Condominio'].fillna(0, inplace=True)
alugueis.info()

alugueis['Condominio'] = [0.0 if tipo != 'Apartamento' and pd.isna(condominio) else condominio for tipo, condominio in zip(alugueis['Tipo'], alugueis['Condominio'])]
alugueis.dropna(subset=['Condominio'], inplace=True)

alugueis['IPTU'].fillna(0, inplace=True)

alugueis.to_csv('/home/laumzav/PycharmProjects/Python_study/AlCuOn/Pandas/aluguel_tratado.csv', index=False)