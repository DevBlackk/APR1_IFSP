number_list = []
list_cubed = []
N = int(input("Digite um número: "))

for num in range(N):
    number = int(input(f"Digite o número {num + 1}: "))
    number_list.append(number)
    list_cubed.append(number ** 3)

print(f"Lista original: {number_list}")
print(f"Lista com os números elevados ao cubo: {list_cubed}")