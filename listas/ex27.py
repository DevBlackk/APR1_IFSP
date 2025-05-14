'''N = int(input("Digite um número: "))

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
print(f"Soma das sequências: {sequence_sum}")'''

N = int(input("Digite um número: "))

number = []
sequence_a = []
sequence_b = []
sequence_sum = []

print("Digite o número da sequncia A")
i = 0
while i < N:
    number = int(input(f"Digite o número {i + 1}: "))
    sequence_a.append(number)
    i += 1

print("Digite o número da sequncia B")
i = 0
while i < N:
    number = int(input(f"Digite o número {i + 1}: "))
    sequence_b.append(number)
    i += 1

i = 0
while i < N:
    sequence_sum.append(sequence_a[i] + sequence_b[i])
    i += 1

print("Sequência A: ")
i = 0
while i < len(sequence_a):
    print(sequence_a[i], end=" ")
    i += 1
print()

print("Sequência B: ")
i = 0
while i < len(sequence_b):
    print(sequence_b[i], end=" ")
    i += 1
print()

print("Soma das sequências: ")
i = 0
while i < len(sequence_sum):
    print(sequence_sum[i], end=" ")
    i += 1
print()