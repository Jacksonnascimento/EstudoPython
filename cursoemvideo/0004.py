# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 23:05:20 2019

@author: jacks
"""

dados = input("Escreva algo: ")
print("O tipo primitivo desse valor é {}".format(type(dados)))
print("Só tem espaços? {}".format(dados.isspace()))
print("É um número? {}".format(dados.isnumeric()))
print("É alfabético? {}".format(dados.isalpha()))
print("É alfabumérico? {}".format(dados.isalnum()))
print("Está em maiúsculas? {}".format(dados.isupper()))
print("Está em minúsculas? {}".format(dados.islower()))
print("Está capitalizado? {}".format(dados.istitle()))
