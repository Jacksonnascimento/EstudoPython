#Escreva um programa que compare se duas sequências digitadas pelo usuário são iguais
import re 
import MySQLdb
sequencia = input("Escreva uma sequência de caracteres: ")
sequencia2 = input("Escreva outra sequência de caracteres: ")

"""if sequencia == sequencia2:
	print("Sequências iguais")
else:
	print("Sequências diferentes")""" 
busca = re.match(sequencia, sequencia2)

if busca:
	print("Sequências iguais")
else:
	print("Sequências diferentes")

