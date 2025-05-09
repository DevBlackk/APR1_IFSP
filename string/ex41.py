'''5. Faça um programa que recebe uma frase e retorna o número de palavras
que a frase contém.'''

frase = input("Digite uma frase: ")

palavra = 1
dentro_palavra = True

for caractere in frase:
    if caractere == ' ' and dentro_palavra:
        dentro_palavra = False
    elif caractere != ' ' and not dentro_palavra:
        palavra += 1
        dentro_palavra = True

if not frase.strip():
    palavra = 0

print(f"\nA frase contém {palavra} palavras.")