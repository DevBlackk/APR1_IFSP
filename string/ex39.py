'''3. Escreva um programa que verifique se duas strings fornecidas pelo
usuário são iguais e mostre o total de caracteres de cada uma delas.
Diferencie letras maiúsculas das minúsculas.'''

str_1 = input("Digite a primeira string: ")
str_2 = input("Digite a segunda string: ")

print(f"\nTamanho da primeira string: {len(str_1)} caracteres")
print(f"Tamanho da segunda string: {len(str_2)} caracteres")

if str_1 == str_2:
    print("\nAs string são iguais!")
else:
    print("\nAs strings são diferentes!")