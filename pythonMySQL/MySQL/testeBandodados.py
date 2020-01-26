# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 20:06:17 2019

@author: jacks
"""
import pymysql

host = "localhost"
user = "aplicacao"
senha = "@jn87519023"
bancodados = "informacoes"
porta = 3306

con = pymysql.connect(host, user, senha, bancodados, porta)

c = con.cursor(pymysql.cursors.DictCursor)

def insert (valores, tabela):
    global c, con
    '''#insert into cursos
    values('15', 'Ciência da Computação');'''
    query = "Insert into " + tabela + " values (" + valores + " );"
    
    print(query)
    c.execute(query)
    con.commit()

#select * from pessoa where id_pessoa = 1;    
def select(campos, tabela, condicao = None):
    
    global c
    
    query = "select " + campos + " from " + tabela
    if(condicao):
        query = query + " where " + condicao
    
    print(query)
    c.execute(query)
    return c.fetchall()
'''
for i in range(0, 5):
    nome = input("Digite seu nome: ")
    nome = "'" + nome + "',"
    curso = input("Digite seu curso: ")
    curso = "'" + curso + "'"
    valor = "DEFAULT, " + nome + curso

    insert(valor, "pessoa")
'''
condicao = ""
print("Caso queira encerrar o programa, digite 'fechar'")
while (condicao != "fechar"):
    
    condicao = input("Digita o ID da pessoa: ")
    
    if(condicao != "fechar"):
        
         campos = "nome" #input("Digita o (s) campo (s): ")         
         condicao = "id_pessoa = " + condicao
         resultado = select(campos, "pessoa", condicao)
         print(resultado[0]["nome"])
    else:
         print("O progrma será fechado...")

#print(resultado[0]["curso"])




