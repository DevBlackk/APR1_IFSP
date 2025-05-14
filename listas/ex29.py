'''N = int(input("Digite um número: "))
list_numbers = []

for num in range(N):
    number = int(input(f"Digite o número {num + 1}: "))
    list_numbers.append(number)
    reversed_list = []
    for i in range(len(list_numbers) - 1, -1, -1):
        reversed_list.append(list_numbers[i])

print(f"Lista invertida: {reversed_list}")
print(f"Lista original: {list_numbers}")'''

N = int(input("Digite um número: "))
list_number = []
reverse_list = []

i = 0
while i < N:
    number = int(input(f"Digite um número: "))
    list_number.append(number)
    i += 1

i = -1
while i >= -len(list_number):
    reverse_list.append(list_number[i])
    i -= 1


print("Lista invertida")
i = 0
while i < len(reverse_list):
    print(reverse_list[i], end=" ")
    i += 1
print()

print("Lista original")
i = 0
while i < len(list_number):
    print(list_number[i], end=" ")
    i += 1