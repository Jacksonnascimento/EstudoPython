primeiro_nome = " Jackson"
sobrenome = "Nascimento"

nome_completo = primeiro_nome + " " + sobrenome + "\n"

#print(nome_completo)

"""tamanho = len(nome_completo) #contar a quantidade de caracteres
tamanho_primeiro_nome = len(primeiro_nome)

print(tamanho) 
print(tamanho_primeiro_nome)

print(primeiro_nome[0])
print(primeiro_nome[1])

print(primeiro_nome[0:4]) #metade da string """

"""minusculo = nome_completo.lower() #todas as letras em minúsculo
print("Nome em minúsculo: " + minusculo)

maiusculo = nome_completo.upper() #todas as letras em maiúsculo
print("Nome em maiúsculo: " + maiusculo)

print(nome_completo.strip()) #remover espaços no começo e no fim da string
"""
minha_string = "Vamos todo mundo cantar juntos (ueba!)"
#minha_lista = minha_string.split(" ") #converter uma string em uma lista
#print(minha_lista)

busca = minha_string.find("cantar") #buscar substrings
print(busca)
print(minha_string[busca:]) #imprimir da subtring (no caso, "cantar") até o final 
                             
substituir = minha_string.replace("cantar", "dançar") #substituir partes de uma string
print(substituir)