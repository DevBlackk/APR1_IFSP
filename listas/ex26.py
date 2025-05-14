'''4. Crie um programa que leia inicialmente uma sequencia de N números inteiros. 
Depois, o programa deve gerar e mostrar 2 novas listas apartir da primeira: uma 
sem repetição de elementos e outra com oselementos que se repetem na lista original.'''

N = int(input("Digite um número: "))
number_list = []
repeated_numbers = []
unique_numbers = []

# Lê os números
i = 0
while i < N:
    number = int(input("Digite um número: "))
    number_list.append(number)
    i += 1

i = 0
while i < len(number_list):
    found = False
    j = 0
    while j < len(number_list):
        if i != j and number_list[i] == number_list[j]:
            found = True
        j += 1
        
    if found:
        k = 0
        ja_existe = False
        while k < len(repeated_numbers):
            if number_list[i] == repeated_numbers[k]:
                ja_existe = True
            k += 1
            
        if not ja_existe:
            repeated_numbers.append(number_list[i])
    else:
        unique_numbers.append(number_list[i])
    i += 1

print("Lista original: ")
i = 0
while i < len(number_list):
    print(number_list[i], end=" ")
    i += 1
print()

print("Números que se repetem: " )
i = 0
while i < len(repeated_numbers):
    print(repeated_numbers[i], end=" ")
    i += 1
print()

print("Números sem repetição: ")
i = 0
while i < len(unique_numbers):
    print(unique_numbers[i], end=" ")
    i += 1
print()