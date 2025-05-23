'''6. Faça um programa que solicite o nome do usuário e imprima-o na
vertical e em formato de escada.'''

name = input("Digite seu nome: ")
i = 0
while i < len(name):
    print(name[:i - 1])
    i += 1