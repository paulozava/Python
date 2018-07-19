import pandas

alugueis = pandas.read_csv('/home/laumzav/PycharmProjects/Python_study/AlCuOn/Pandas/aluguel.csv', sep=';')

## observando a importação dos dados
alugueis.head() #importa os primeiros
alugueis.tail(n=2) #importa os últimos

## mostrando os tipos de dados
type(alugueis) # que objeto é
alugueis.info() #informações sobre o dataframe do pandas
alugueis.dtypes #mesma informação assima, mas só com os tipos de dados (object=>string; int64=>int; float64=> float) OBS. usar sem parenteses

# embelezando o dataFrame
tipos_dados = pandas.DataFrame(alugueis.dtypes, columns=['Tipos de dados']) #criando um DF para receber os dados
tipos_dados.columns.name = 'Variável' #modificando a coluna de variáveis
tipos_dados

