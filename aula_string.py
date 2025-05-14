frase = "Eu posso ajudar respondendo no fórum!"
soteio = [5 , -4, 3, -8, 11]
acertos = 0

for i in soteio:
    resposta = input(f"Qual o caracter do indice {i} ")
    if resposta == frase[i]:
        print("Você acertou!")
        acertos += 1
    else:
        print(f"Você errou! O caracteres de indice {i} é: {frase[i]}")
print(f"Você acertou {acertos} de {len(soteio)} perguntas.")

ini, fim = 9, 15
texto = "Eu posso ajudar respondendo no fórum!"
fatia = texto[ini:fim]
print("Seja o texto:", texto)
resposta = input(f"Qual o texto entre os indices [{ini}:{fim}] =  ")
if resposta == fatia:
    print("Você acertou!")
else:
    print(f"Você errou! Você ecreveu: {resposta} e o correto é: {fatia}")

texto = "Essa é uma 'string' de teste!"
# print(texto)
# texto[2] = 'S'
# print(texto)

print(f"{texto[0:12]}" + 'S' + f"{texto[13:]}")

word = "zebra"
if word < 'banana':
    print("Your word, " + word + ", comes before banana.")
elif word > 'banana':
    print("Your word, " + word + ", comes after banana.")
else:
    print("Yes, we have no bananas.")

print("apple" < "banana")
print("apple" > "Apple")
print("apple" == "Apple")

palavra = input("Digite uma palavra: ")
vogais = "aeiouAEIOU"
str_sem_vogais = ""
for cada_letra in palavra:
    if cada_letra not in vogais:
        str_sem_vogais += cada_letra
print(f"A palavra sem vogais é: {str_sem_vogais}")

palavra = input("Digite uma palavra: ")
caracter = input("Digite um caracter: ")
contagem = 0
for letra in palavra:
    if letra == caracter:
        contagem += 1
print(f"A letra '{caracter}' aparece {contagem} vezes na palavra '{palavra}'.")

palavra = input("Digite uma palavra: ")
caractere = input("Digite um caracter a ser encontrado: ")
indice = 0
existe_letra = False
while indice < len(palavra) and not existe_letra:
    if palavra[indice] == caractere:
        existe_letra = True
    else:
        indice = indice + 1
if existe_letra:
    print(f"A primeira ocorrência do caractere {caractere} na palavra {palavra} está na posição {indice}")
else:
    print(f"Não há ocorrência do caractere {caractere} na palavra {palavra}!")

import string
print(string.ascii_lowercase)
print(string.ascii_uppercase)
print(string.digits)
print(string.punctuation)