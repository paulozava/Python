import pandas as pd

alugueis = pd.read_csv('/home/laumzav/PycharmProjects/Python_study/AlCuOn/Pandas/aluguel.csv', sep=';')

alugueis.head(5)

tipos = alugueis['Tipo'].drop_duplicates()
# somente apartamento
# minha solucao
selecao = list(alugueis['Tipo'] == 'Apartamento')
total_1 = selecao.count(True)
# instrutor
selecao = alugueis['Tipo'] == 'Apartamento'
n1 = alugueis[selecao].shape[0]

correto = total_1 == n1

# casa, casa de condominio e casa de vila
# minha solucao
selecao = [x in ('Casa', 'Casa de Condomínio', 'Casa de Vila') for x in alugueis['Tipo']]
total_2 = selecao.count(True)
# instrutor
selecao = (alugueis['Tipo'] == 'Casa') | (alugueis['Tipo'] == 'Casa de Condomínio') | (alugueis['Tipo'] == 'Casa de Vila')
n2 = alugueis[selecao].shape[0]

total_2 == n2

# área entre 60-100 m2
# minha solucao
selecao = [60<=x<=100 for x in alugueis['Area']]
total_3 = selecao.count(True)
# instrutor
selecao = (alugueis['Area'] >= 60) & (alugueis['Area'] <= 100)
n3 = alugueis[selecao].shape[0]

total_3 == n3



# pelo menos 4 quartos e aluguel menor que 2mil
# minha solucao
selecao = [True if quarto >= 4 and valor < 2000 else False for quarto, valor in zip(alugueis['Quartos'], alugueis['Valor'])]
total_4 = selecao.count(True)
# instrutor
selecao = (alugueis['Quartos'] >= 4) & (alugueis['Valor'] < 2000)
n4 = alugueis[selecao].shape[0]

total_4 == n4

#resposta
resposta = f'somente apartamento: {total_1} imoveis; \ncasa, casa de condominio e casa de vila: {total_2} imoveis; \nárea entre 60-100 m2: {total_3} imoveis; \npelo menos 4 quartos e aluguel menor que 2mil: {total_4} imoveis'
print(resposta)

total_4 = 1
resposta = f'somente apartamento: {total_1} imoveis; \ncasa, casa de condominio e casa de vila: {total_2} imoveis; \nárea entre 60-100 m2: {total_3} imoveis; \npelo menos 4 quartos e aluguel menor que 2mil: {total_4} imove{"is" if total_4 > 1 else "l"}'
print(resposta)