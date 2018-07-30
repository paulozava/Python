import pandas as pd

alugueis = pd.read_csv('/home/laumzav/PycharmProjects/Python_study/AlCuOn/Pandas/aluguel_tratado.csv')
tipos = alugueis['Tipo'].drop_duplicates()
alugueis['TipoConsolidado'] = alugueis['Tipo'].replace(to_replace=['Quitinete', 'Casa de Vila', 'Casa de Condomínio'], value='Casa').replace(to_replace=['Flat', 'Loft'], value='Apartamento')
alugueis['PrecoM2'] = alugueis['Valor'] / alugueis['Area']
alugueis['PrecoM2'] = alugueis['PrecoM2'].round(decimals=2)
alugueis['Despesas'] = alugueis['Valor'] + alugueis['Condominio'] + alugueis['IPTU']
