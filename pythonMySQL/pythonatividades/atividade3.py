"""Escreva um programa que receba uma 
sequência digitada pelo usuário e a salve num arquivo no formato fasta.   """
texto = input("Digite um texto: ") 

arquivo = open("arquivoAtividade3.fasta", "w")

arquivo.write(">seq\n") 
arquivo.write(texto) 
arquivo.close()