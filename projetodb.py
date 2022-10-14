import matplotlib.pyplot as plt
import pymongo
import pandas as pd

y =[]
conexao = pymongo.MongoClient("mongodb://localhost:27017/")

meu_banco = conexao['projeto4bi']

colecao = meu_banco['eleições']

pd.set_option('display.max_columns', None) # coluna
pd.set_option('display.max_rows', None) # linha
table = pd.read_csv("ccont_2t_AC_271020181441.csv", delimiter=';',encoding="windows-1252")

municipio = table["NM_MUNICIPIO"]
secoes = table["NR_ZONA"]

'''for i in range(len(secoes)):
    c = colecao.insert_one({"seções": int(secoes[i])})
    print(c)
'''
'''
for i in range(len(municipio)):
    c = colecao.insert_one({"municipios": str(municipio[i])})
    print(c)
'''
lista = []
for i in range(len(municipio)):
    lista.append(str(municipio[i]))

lista_set = set(lista)


grup = table.groupby('NM_MUNICIPIO').sum()
z = grup['NR_ZONA']

for i in range(len(lista_set)):
    y.append(z[i])

# x axis values
x = ['ACRELÂNDIA', 'ASSIS BRASIL', 'BRASILÉIA', 'BUJARI', 'CAPIXABA', 'CRUZEIRO DO SUL', 'EPITACIOLÂNDIA', 'FEIJÓ', 'JORDÃO', 'MANOEL URBANO', 'MARECHAL THAUMATURGO', 'MÂNCIO LIMA', 'PLÁCIDO DE CASTRO', 'PORTO ACRE', 'PORTO WALTER', 'RIO BRANCO', 'RODRIGUES ALVES', 'SANTA ROSA DO PURUS', 'SENA MADUREIRA', 'SENADOR GUIOMARD', 'TARAUACÁ', 'XAPURI']
# corresponding y axis values


# plotting the points
axes = plt.gca()
plt.bar(x,y, color="red")

# naming the x axis
plt.xlabel('x - Municípios')
# naming the y axis
plt.ylabel('y - Seções')

# giving a title to my graph
plt.title('Grafico gerado!')
plt.xticks(rotation=90)

# function to show the plot
plt.show()



