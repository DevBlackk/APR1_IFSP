N = int(input("Digite um total de números: "))
list_numbers = []
numbers_even = 0
numbers_odd = 1

i = 0
while i < N:
    list_numbers.append(int(input("Digite um número: ")))
    i += 1

j = 0
while j < len(list_numbers):
    if list_numbers[j] % 2 == 0:
        numbers_even += list_numbers[j]
    else:
        numbers_odd *= list_numbers[j]
    j += 1

print(f"A lista é:")
j = 0
while j < len(list_numbers):
    print(list_numbers[j], end=" ")
    j += 1

print()
print(f"A soma dos números pares é: {numbers_even}")
print(f"A multiplicação dos números ímpares é: {numbers_odd}")