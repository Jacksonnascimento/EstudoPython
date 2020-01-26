#visualização de dados com Python
import matplotlib.pyplot as plt
    
x1 = [1, 3, 5, 7, 9]
y1 = [2, 3, 7, 1, 0]
z = [200, 25, 400, 330, 100]   #tamanho do círculo
'''
x2 = [2, 4, 6, 8, 10]
y2 = [5, 1 , 3, 7, 4]'''

titulo = "Scatterplot: gráfico de dispersão"
eixox = "Eixo X"
eixoy = "Eixo Y"

#título do gráfico
plt.title(titulo)

#legenda dos eixos X e Y
plt.xlabel(eixox)
plt.ylabel(eixoy)

plt.plot(x1, y1, color = "000000", linestyle = "--") #gráfico de linhas
plt.scatter(x1, y1, label = "Meus pontos", color = "b", marker = ".", s = z) #scartterplot e plot juntos mostram os pontos e as linhas ligando os pontos
plt.legend()
plt.savefig("figura1.png", dpi = 300)  #salvar figura
'''plt.bar(x1, y1, label = "Grupo 1")  #gráfico de barras | label - leganda 
plt.bar(x2, y2, label = "Grupo 2")  # x1, y1 e x2, y2 para fazer comparação de gráficos com barras
plt.legend() #plotar a legenda '''

# plt.show() #exibir no Sublime Text 3
    

 