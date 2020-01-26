""" Escreva um programa que exiba um menu e pergunte o que o usuário deseja fazer. 
Se o usuário digitar 1, o programa deve chamar uma função que lê um arquivo de texto.
 o usuário apertar 2, o programa deve imprimir o conteúdo do arquivo 
 lido anteriormente. Se o usuário apertar três o programa deve ser fechado"""
def ler():
	nome = input("Digite o nome do arquivo: ")
	arquivo = open(nome) 
	return arquivo

def imprimir(arquivo):
	linhas = arquivo.readlines()

	for linha in linhas:
		print(linha.strip())
		arquivo.close()
	

opcao = " "

while opcao != 3:
	opcao = int(input("Digite uma opção (número): "))
	if opcao == 1:
		arquivo = ler()
	elif opcao == 2:
		imprimir(arquivo)
	elif opcao == 3:
		arquivo.close()
		print("O programa será fechado")
	else:
		print("Opção inválida")




