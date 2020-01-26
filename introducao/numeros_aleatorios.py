import random 

numero = random.randint(0, 10) #número aleatório de x (0, no caso) a y (10, no exemplo)
print(numero)

lista_numero = [10, 500, 400, 29, 1, 6523, 42]
numero = random.choice(lista_numero) #selecionar o número de uma lista
print(numero)