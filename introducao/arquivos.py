"""arquivo = open("arquivo.txt")

#linhas = arquivo.readlines() #ler arquivo e o armazenar em uma lista
#print(linhas)

#linha = arquivo.readline() #ler uma linha 
#print(linha)

arquivo_inteiro = arquivo.read() #ler arquivo inteiro 
print(arquivo_inteiro) """ 

#novo_arquivo = open("arquivo2.txt", "w") #escrever no arquivo (apaga o conteúdo anterior)

novo_arquivo = open("arquivo2.txt", "a") #adicionar o novo conteúdo ao fim do arquivo
novo_arquivo.write("Este é o meu novo arquivo\n") #escrever no arquivo

novo_arquivo.close()  #fechar arquivo

novo_arquivo = open("arquivo2.txt")
texto = novo_arquivo.read()
print(texto)
novo_arquivo.close()
