'''4. Escreva um programa que reconhece se uma string é um palíndromo.
Exemplo: arara, ovo, reter.'''

texto = input("Digite uma palavra: ")

texto = texto.lower().replace(" ", "")

if texto == texto[::-1]:
    print("O texto é um políndromo")
else:
    print("O texto não é um políndromo")

text = input("Digite uma palavra: ")
i = 0
j = len(text) - 1

palindromo = True
while i < len(text) and palindromo and i < j:
    if text[i] != text[j]:
        palindromo = False
    i += 1
    j -= 1
if palindromo == True:
    print("É um palíndromo")
else:
    print("Não é um palíndromo")