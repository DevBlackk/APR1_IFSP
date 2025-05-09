list_number = []
greater_number = 0
smaller_number = 0
sum_numbers = 0
numbers_odd = []
numbers_greater_than_18 = []

i = 0
while i < 10:
    numbers = int(input("Digite um número: "))
    list_number.append(numbers)
    i += 1

j = 0
greater_number = smaller_number = list_number[j]
while j < len(list_number):
    if list_number[j] > greater_number:
        greater_number = list_number[j]
    if list_number[j] < smaller_number:
        smaller_number = list_number[j]
    sum_numbers += list_number[j]
    
    if list_number[j] % 2 != 0:
        numbers_odd.append(list_number[j])
    
    if list_number[j] > 18:
        numbers_greater_than_18.append(list_number[j])
    j += 1


print(f"Os números digitados foi: {list_number}")
print(f"O maior número é: {greater_number}")
print(f"O maior número é: {smaller_number}")
print(f"A soma dos números é: {sum_numbers}")
print(f"Os números ímpares são: {numbers_odd}")
print(f"Os números maiores que 18 são: {numbers_greater_than_18}")
