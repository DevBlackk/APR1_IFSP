N = int(input("Digite um número: "))
list_numbers = []

for num in range(N):
    number = int(input(f"Digite o número {num + 1}: "))
    list_numbers.append(number)

original_list = list_numbers[:]
list_numbers_odd = []
list_numbers_even = []
for i in range(len(list_numbers)):
    if list_numbers[i] % 2 != 0:
        list_numbers[i] = -1
    else:
        list_numbers[i] = +1

print(f"Lista original: {original_list}")
print(f"Lista subistituida: {list_numbers}")
