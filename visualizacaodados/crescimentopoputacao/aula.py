# Crescimento da População Brasileira 1980-2016
# DataSus
import matplotlib.pyplot as plt

dados = open("populacao-brasileira.csv").readlines()

x = []
y = []
                                # ranger() cria uma lista que vai de zero até o tamanho final dos dados
for i in range(len(dados)): #função len() pega o tamanho de dados, ou seja, quantas linhas ele tem
	if i != 0:    #ignorar a linha zero                    
		linha = dados[i].split(";") #split(";") separar por ponto e vírgula 
		x.append(int(linha[0])) #adicionar valor de linha na posição 0 / posição 0 = ano 
		y.append(int(linha[1])) #adicionar valor de linha na posição 1 / posição 1 = população 

plt.bar(x, y, color="#e4e4e4")
plt.plot(x, y, color='k', linestyle="--")

plt.title("Crescimento da População Brasileira 1980-2016")
plt.xlabel("Ano")
plt.ylabel("População x100.000.000")
#plt.show()
plt.savefig("populacao_brasileira.png", dpi=300)

