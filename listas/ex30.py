'''N = int(input("Digite um número: "))
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
print(f"Lista subistituida: {list_numbers}")'''

N = int(input("Digite um número: "))
list_numbers = []
original_numbers = []

i = 0
while i < N:
    number = int(input(f"Digite um número {i + 1}: "))
    list_numbers.append(number)
    original_numbers.append(number)
    i += 1

i = 0
while i < len(list_numbers):
    if list_numbers[i] % 2 == 0:
        list_numbers[i] = +1
    else:
        list_numbers[i] = -1
    i += 1

print("Sequncia alterada:")
i = 0
while i < len(list_numbers):
    print(list_numbers[i], end=" ")
    i += 1
print()

print("Sequencia original")
i = 0
while i < len(original_numbers):
    print(original_numbers[i], end=" ")
    i += 1
print()