import pandas as pd
import matplotlib.pyplot as plt

alugueis = pd.read_csv('/home/laumzav/PycharmProjects/Python_study/AlCuOn/Pandas/aluguel_tratado.csv')

grupo_bairros = alugueis.groupby('Bairro')
sumario = pd.DataFrame(columns=['Bairro', 'Aluguel_medio'])
bairros, valores = [], []
for bairro, itens in grupo_bairros:
    bairros.append(bairro)
    valores.append(itens['Valor'].mean().round(2))

sumario['Bairro'] = bairros
sumario['Aluguel_medio'] = valores

grupo_bairros['Valor'].mean().round(2)

bairros = ['Barra da Tijuca', 'Botafogo', 'Copacabana', 'Flamengo', 'Ipanema', 'Leblon', 'Tijuca']

so_bairros = alugueis[alugueis['Bairro'].isin(bairros)]
grupo_bairros = so_bairros.groupby('Bairro')
sumario = grupo_bairros[['Valor', 'Condominio']].mean().round(2)
sumario.describe().round(2)

plt.rc('figure', figsize=(20,10))
fig = grupo_bairros['Valor'].mean().plot.bar(color = 'red')
fig.set_ylabel('Media aluguel')


precos = pd.DataFrame([['Feira', 'Cebola', 2.5], ['Mercado', 'Cebola', 1.99],['Supermercado', 'Cebola', 1.69], ['Feira', 'Tomate', 4], ['Mercado', 'Tomate', 3.29], ['Supermercado', 'Tomate', 2.99], ['Feira', 'Batata', 4.2], ['Mercado', 'Batata', 3.99], ['Supermercado', 'Batata', 3.69]], columns = ['Local', 'Produto', 'Preço'])
produtos = precos.groupby('Produto')
estatisticas = ['mean', 'std', 'min', 'max']
nomes = {'mean':'Média', 'std':'Desvio Padrão', 'min':'Mínimo', 'max':'Máximo'}
produtos.aggregate(estatisticas).rename(columns=nomes).round(2)

alugueis.info()
classes = [0,2,4,6,100]
quartos = pd.cut(alugueis['Quartos'], classes)
quartos_classe = pd.value_counts(quartos)
labels = ['1-2 quartos', '3-4 quartos', '5-6 quartos', '7+ quartos']
labels_quartos = list(zip(labels, quartos_classe))
sumario = pd.DataFrame(labels_quartos, columns=['Quartos', 'Quantidade'])
sumario

classes = [0,2,4,6,100]
labels = ['1-2 quartos', '3-4 quartos', '5-6 quartos', '7+ quartos']
quartos = pd.cut(alugueis['Quartos'], classes, labels=labels)
quartos_classe = pd.value_counts(quartos)
