lines = int(input("Enter the number of lines: "))
colons = int(input("Enter the number of columns: "))
matriz = []

for i in range(lines):
    line = []
    for j in range(colons):
        x = ((i + 1) * (j + 1))
        line.append(x)
    matriz.append(line)

for i in range(lines):
    for j in range(colons):
        print(matriz[i][j], end=" ")
    print()