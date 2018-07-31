import pandas as pd

alugueis = pd.read_csv('/home/laumzav/PycharmProjects/Python_study/AlCuOn/Pandas/aluguel_tratado.csv')

alugueis['DespesasBrutas'] = alugueis['Valor'] + alugueis['Condominio'] + alugueis['IPTU']
alugueis['DespesasLiquidas'] = alugueis['Valor'] + alugueis['Condominio']
alugueis.info()

del alugueis['DespesasLiquidas']
alugueis.info()

alugueis.pop('DespesasBrutas')
alugueis.info()

alugueis.drop(columns='IPTU', inplace=True)
alugueis.info()


alugueis.Suites.unique()
alugueis.Tipo.value_counts()


m1 = 'CCcCCccCCCccCcCccCcCcCCCcCCcccCCcCcCcCcccCCcCcccCc'
m2 = 'CCCCCccCccCcCCCCccCccccCccCccCCcCccCcCcCCcCccCccCc'
m3 = 'CccCCccCcCCCCCCCCCCcccCccCCCCCCccCCCcccCCCcCCcccCC'
m4 = 'cCCccCCccCCccCCccccCcCcCcCcCcCcCCCCccccCCCcCCcCCCC'
m5 = 'CCCcCcCcCcCCCcCCcCcCCccCcCCcccCccCCcCcCcCcCcccccCc'

moedas = pd.DataFrame(columns=['m1','m2','m3','m4','m5'])

moedas['m1'] = m1.replace('C', 'Cara ').replace('c', 'Coroa ').strip().split(' ')
moedas['m2'] = m2.replace('C', 'Cara ').replace('c', 'Coroa ').strip().split(' ')
moedas['m3'] = m3.replace('C', 'Cara ').replace('c', 'Coroa ').strip().split(' ')
moedas['m4'] = m4.replace('C', 'Cara ').replace('c', 'Coroa ').strip().split(' ')
moedas['m5'] = m5.replace('C', 'Cara ').replace('c', 'Coroa ').strip().split(' ')

sumario = pd.DataFrame(index=['Cara', 'Coroa'], columns=['m1','m2','m3','m4','m5'])

for index in ['m1','m2','m3','m4','m5']:
    sumario[index] = moedas[index].value_counts()

for index in ['m1','m2','m3','m4','m5']:
    sumario[index] = sumario[index] / sum(sumario[index])