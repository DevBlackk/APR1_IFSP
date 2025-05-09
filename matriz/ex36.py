M = int(input("Enter the number of rows: "))
N = int(input("Enter the number of columns: "))
matriz = []

for i in range(M):
    line = []
    for j in range(N):
        line.append((i + 1) * (j + 3))
    matriz.append(line)

print("\nMatrix:")
for i in range(M):
    for j in range(N):
        print(f"{matriz[i][j]:4}", end="")
    print()

different_sum = 0
for i in range(M):
    for j in range(N):
        if matriz[i][j] != matriz[j][i]:
            different_sum += 1

if different_sum == 0:
    print("\nThe matrix is symmetric.")
else:
    print("\nThe matrix is not symmetric.")