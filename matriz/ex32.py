M = int(input("Enter the number of value: "))
matriz = []

for i in range(M):
    linha = []
    for j in range(M):
        x = int(input(f"Inform the element [{i}][{j}]: "))
        linha.append(x)
    matriz.append(linha)
    print(matriz)

sum_diagonal = 0 
for i in range(M):
    for j in range(M):
        if i == j:
            diagonal_elements = []
            diagonal_elements.append(matriz[i][j])
            print(matriz[i][j], end = " ")
    sum_diagonal += matriz[i][i]
    print()

print(f"Sum of diagonal elements:{sum_diagonal}")
