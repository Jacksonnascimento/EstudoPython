idade = int(input("Digite a sua idade: "))

if idade >= 18:
	print("Você é maior de idade")
elif idade > 0 and idade < 18:
	print("Você é menor de idade")
else:
	print("Idade inválida")