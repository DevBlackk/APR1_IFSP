'''number_list = []
list_cubed = []
N = int(input("Digite um número: "))

for num in range(N):
    number = int(input(f"Digite o número {num + 1}: "))
    number_list.append(number)
    list_cubed.append(number ** 3)

print(f"Lista original: {number_list}")
print(f"Lista com os números elevados ao cubo: {list_cubed}")'''

N = int(input("Digite um número: "))
number_list = []
list_cubed = []

i = 0
while i < N:
    number = int(input(f"Digite um número {i + 1}: "))
    number_list.append(number)
    i += 1

i = 0
while i < len(number_list):
    list_cubed.append(number_list[i] ** 3)
    i += 1

print(f"Lista original:")
i = 0
while i < len(number_list):
    print(number_list[i], end=" ")
    i += 1
print()
print(f"Lista com os números elevados ao cubo:")
i = 0
while i < len(list_cubed):
    print(list_cubed[i], end=" ")
    i += 1
print()