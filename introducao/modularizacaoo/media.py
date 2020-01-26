# media, mediana, moda
#from statistics import *   #importar metodos para calcular média, mediana e moda

def media(lista):
	#media = mean(lista)  #calcular media
	media = sum(lista)/float(len(lista))  #sum - somar todos os elementos de uma lista/ len - tamanho da lista 

	return media

def mediana(lista):
	#return median(lista)
	lista_ordenada = sorted(lista) #ordenar lista
	t = len(lista_ordenada)

	if t % 2 == 0:
		mediana = (lista_ordenada[int(t/2)] + lista_ordenada[int((t/2)-1)])/2
	elif t % 2 == 1:
		mediana = lista_ordenada[int((t/2))]

	return mediana


