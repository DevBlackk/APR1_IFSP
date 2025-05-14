'''10. Escreva um programa que solicite ao usuário a entrada de um número
inteiro positivo ou negativo e mostre a quantidade de dígitos desse
número.'''

number = input("Digite um número inteitro ou negativo: ")
digit = '0123456789'
if number[0] == '-':
    i = 1
    while  i < len(number):
        if number[i] in digit:
            count += 1
        i += 1
else:
    i = 0
    while i < len(number):
        if number[i] in digit:
            count += 1
        i += 1

print(f"Total de digitos: {count}")