N = int(input("Digite um número: "))
number_list = []
repeated_numbers = []
unique_numbers = []
i = 0
while i < N:
    number = int(input("Digite um número: "))
    number_list.append(number)
    i += 1

j = 0
while j < len(number_list):
    if repeated_numbers == 0:
        repeated_numbers.append(number_list[j])
    
    j += 1

print("Lista de números unicos: ")
l = 0
while l < len(unique_numbers):
    print(unique_numbers[l], end=' ')
    l += 1
print()

print("Lista de números repetidos: ")
l = 0
while l < len(repeated_numbers):
    print(repeated_numbers[l], end=" ")
    l += 1
print()

print("Lista original de números: ")
l = 0
while l < len(number_list):
    print(number_list[l], end=" ")
    l +=1

'''
    found = False
    k = j + 1
    while k < len(number_list):
        if len(repeated_numbers) == 0:
            found = True
        k += 1
        
    if found == True:
        repeated_numbers.append(number_list[j])
    else:
        m = 0
        while m < len(repeated_numbers):
            if repeated_numbers[m] != number_list[j]:
                unique_numbers.append(number_list[j])
            m += 1
'''