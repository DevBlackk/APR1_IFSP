'''8. Faça um programa que leia duas matrizes de mesma ordem MxN e mostre as duas
matrizes originais e a matriz resultante A - B, em formato matricial.'''

M = int(input("Digite o valor das colunas: "))
N = int(input("Digite o valor das linhas: "))
matriz_a = []
matriz_b = []
result_matriz = []


for i in range(M):
    line = []
    for j in range(N):
        line.append((i + 1) * (j + 25))
    matriz_a.append(line)

for i in range(M):
    line = []
    for j in range(N):
        line.append((i + 1) * (j + 5))
    matriz_b.append(line)

for i in range(M):
    line = []
    for j in range(N):
        value = matriz_a[i][j] - matriz_b[i][j]
        line.append(value)
    result_matriz.append(line)

print("Matriz A: ")
for i in range(M):
    for j in range(N):
        print(f"{matriz_a[i][j]:4}", end="")
    print()

print("Matriz B: ")
for i in range(M):
    for j in range(N):
        print(f"{matriz_b[i][j]:4}", end="")
    print()

print(f"Maretiz resultande entre A - B: ")
for i in range(M):
    for j in range(N):
        print(f"{result_matriz[i][j]:4}", end="")
    print()