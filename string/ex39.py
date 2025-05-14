'''3. Escreva um programa que verifique se duas strings fornecidas pelo
usuário são iguais e mostre o total de caracteres de cada uma delas.
Diferencie letras maiúsculas das minúsculas.'''

str_1 = input("Digite a primeira string: ")
str_2 = input("Digite a segunda string: ")


if str_1 == str_2:
    print("\nAs string são iguais!")
else:
    print("\nAs strings são diferentes!")

character_str_1 = 0
while character_str_1 < len(str_1):
    character_str_1 = character_str_1 + 1

character_str_2 = 0
while character_str_2 < len(str_2):
    character_str_2 = character_str_2 + 1

print(f"\nTamanho da primeira string: {character_str_1} caracteres")
print(f"Tamanho da segunda string: {character_str_2} caracteres")