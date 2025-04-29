N = int(input("Digite um número: "))

sequence_a = []
sequence_b = []
sequence_sum = []

print("Digite os números da sequência A")
for i in range(N):
    number = int(input(f"Digite o número {i + 1}: "))
    sequence_a.append(number)

print("Digite os números da sequência B")
for i in range(N):
    number = int(input(f"Digite o número {i + 1}: "))
    sequence_b.append(number)

for i in range(N):
    sequence_sum.append(sequence_a[i] + sequence_b[i])

print(f"Sequência A: {sequence_a}")
print(f"Sequência B: {sequence_b}", )
print(f"Soma das sequências: {sequence_sum}")