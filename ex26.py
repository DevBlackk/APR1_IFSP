N = int(input("Digite um número: "))
number_list = []

i = 0
while i < N:
    number = int(input("Digite um número: "))
    number_list.append(number)
    i += 1

unique_numbers = []
repeated_numbers = []

for num in number_list:
    count = 0
    for other_num in number_list:
        if num == other_num:
            count += 1
    
    if count == 1:
        if num not in unique_numbers:
            unique_numbers.append(num)
    elif count > 1:
        if num not in repeated_numbers:
            repeated_numbers.append(num)

print(f"Lista original: {number_list}")
print(f"Lista sem repetição: {unique_numbers}")
print(f"Lista com elementos repetidos: {repeated_numbers}")