M = int(input("Enter the number of lines: "))
N = int(input("Enter the number of columns: "))
matriz = []

for i in range(M):
    line = []
    for j in range(N):
        x = ((i + 1) * (j + 3))
        line.append(x)
    matriz.append(line)
    print(matriz)

print("\nMatriz Original:")
for i in range(M):
    for j in range(N):
        print(f"{matriz[i][j]:4}", end="")
    print()

print("\nMatriz Transposta:")
for j in range(N):
    for i in range(M):
        print(f"{matriz[i][j]:4}", end="")
    print()
