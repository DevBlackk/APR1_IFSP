M = int(input("Enter the number of lines: "))
N = int(input("Enter the number of columns: "))
matriz_1 = []
matriz_2 = []
matriz_sum = [ ]

for i in range(M):
    line = []
    for j in range(N):
        x = ((i + 1) * (j + 1))
        line.append(x)
    matriz_1.append(line)

for i in range(M):
    line = []
    for j in range(N):
        x = ((i + 1) * (j + 1))
        line.append(x)
    matriz_2.append(line)

for i in range(M):
    line_sum = []
    for j in range(N):
        sum = matriz_1[i][j] + matriz_2[i][j]
        line_sum.append(sum)
    matriz_sum.append(line_sum)

print("\nMatriz 1:")
for i in range(M):
    for j in range(N):
        print(f"{matriz_1[i][j]:4}", end=" ")
    print()

print("\nMatriz 2:")
for i in range(M):
    for j in range(N):
        print(f"{matriz_2[i][j]:4}", end=" ")
    print()

print("\nMatriz Soma:")
for i in range(M):
    for j in range(N):
        print(f"{matriz_sum[i][j]:4}", end=" ")
    print()