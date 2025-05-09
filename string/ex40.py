'''4. Escreva um programa que reconhece se uma string é um palíndromo.
Exemplo: arara, ovo, reter.'''

texto = input("Digite uma palavra: ")

texto = texto.lower().replace(" ", "")

if texto == texto[::-1]:
    print("O texto é um políndromo")
else:
    print("O texto não é um políndromo")