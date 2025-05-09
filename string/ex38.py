'''2. Escreva um programa que remove todas as ocorrências de uma letra de
uma string. A string e a letra devem ser fornecidas pelo usuário.'''

texto = input("Digite uma string: ")
letra = input("Digite uma letra: ")

i = 0
while i < len(texto):
    if texto[i] == letra:
        texto = texto[:i] + texto[i + 1:]
    else:
        i += 1
print(f"A string sem a letra {letra} é: {texto}")