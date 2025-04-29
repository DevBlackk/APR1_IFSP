N = int(input("Digite um número: "))
list_numbers = []

for num in range(N):
    number = int(input(f"Digite o número {num + 1}: "))
    list_numbers.append(number)
    reversed_list = []
    for i in range(len(list_numbers) - 1, -1, -1):
        reversed_list.append(list_numbers[i])

print(f"Lista invertida: {reversed_list}")
print(f"Lista original: {list_numbers}")