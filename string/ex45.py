'''7. Faça um programa que permita ao usuário digitar o seu nome e em
seguida o mostre de trás para frente utilizando somente letras
maiúsculas.'''

name = input("Entre com o nome: ")
name = name.upper()

i = -1
while i >= -len(name):
    print(name[i], end=" ")
    i -= 1

