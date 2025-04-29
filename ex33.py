order = int(input("Enter order of the matriz: "))
matriz = []

for i in range(order):
    line = []
    for j in range(order):
        if i == j:
            line.append(1)
        else:
            line.append(0)
    matriz.append(line)

for i in range(order):
    for j in range(order):
        print(f"{matriz[i][j]:2}", end=" ")
    print()