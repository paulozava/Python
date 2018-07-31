import pandas as pd
import matplotlib.pyplot as plt
plt.rc('figure', figsize=(14,6))

alugueis = pd.read_csv('/home/laumzav/PycharmProjects/Python_study/AlCuOn/Pandas/aluguel_tratado.csv')


alugueis.boxplot(['Valor'])
corte = alugueis[alugueis['Valor'] <= 100000.00]
corte.boxplot(['Valor'])

q1 = alugueis['Valor'].quantile(.25)
q3 = alugueis['Valor'].quantile(.75)
iiq = q3 - q1
limite_inferior = q1 - 1.5 * iiq
limite_superior = q3 + 1.5 * iiq
selecao = (alugueis['Valor'] >= limite_inferior) & (alugueis['Valor'] <= limite_superior)
corte = alugueis[selecao]
corte.boxplot(['Valor'])
corte.hist(['Valor'])

grupo_tipo = alugueis.groupby('Tipo')
q1 = grupo_tipo['Valor'].quantile(.25)
q3 = grupo_tipo['Valor'].quantile(.75)
iiq = q3 - q1
limite_inferior = q1 - 1.5 * iiq
limite_superior = q3 + 1.5 * iiq
corte = pd.DataFrame()
for tipo, grupo in grupo_tipo:
    selecao = (grupo['Valor'] >= limite_inferior[tipo]) & (grupo['Valor'] <= limite_superior[tipo])
    selecionados = grupo[selecao]
    corte = pd.concat([corte, selecionados])
corte.boxplot(['Valor'], by=['Tipo'])

corte.to_csv('/home/laumzav/PycharmProjects/Python_study/AlCuOn/Pandas/aluguel_sem_outliers.csv')

area = plt.figure()
g1, g2, g3, g4 = area.add_subplot(2,2,1),area.add_subplot(2,2,2), area.add_subplot(2,2,3), area.add_subplot(2,2,4)
g1.scatter(corte['Valor'], corte['Area'])
g1.set_title('Valor do aluguel por área')
g1.set_ylabel('Valor R$')
g1.set_xlabel('Area m²')

g2.hist(corte['Valor'])
g2.set_title('Valores do aluguel')

g3.hist(corte['Valor'].sample(100).reset_index())

