nome = input("Digite o seu nome: ") 
nota = []
soma = 0.0

print("Seja bem-vindo, " + nome)
arquivo = open("Teste.txt", "a")
arquivo.write("Nome: " + nome + "\n")

for i in range (0, 5):
	nota_input = float(input("Digite o número: "))
	nota.append(nota_input)
	soma = soma + nota_input

media = soma/5
print("Média: ", soma/5)
arquivo.write("Média: " + str(media)) #str converte para string 


for i in nota:
	arquivo.write("\nNota: " + str(i))
	

arquivo.close()