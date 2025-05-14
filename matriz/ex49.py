'''9. Escreva um programa que leia duas matrizes retangulares A e B, com dimensões
MxN e NxP, respectivamente, e calcule o produto entre elas.'''

M = int(input("Digite o número de linhas da matriz A: "))
N = int(input("Digete o número de colunas na matriz A (e linhas de B): "))
P = int(input("Digite o número de colunas na matriz B: "))
matriz_a = []
matriz_b = []
product_matriz = []

print("\nDigite os númeors para a matriz A.")
for i in range(M):
    lines = []
    for j in range(N):
        value = int(input("Digite um número para a Matriz A: "))
        lines.append(value)
    matriz_a.append(lines)
print()

print("\nDigite os númeors para a matriz B.")
for i in range(N):
    lines = []
    for j in range(P):
        value = int(input("Digite um número para a Matriz B: "))
        lines.append(value)
    matriz_b.append(lines)
print()

for i in range(M):
    lines = []
    for j in range(P):
        soma = 0
        for k in range(N):
            soma += matriz_a[i][k] * matriz_b[k][j]
        lines.append(soma)
    product_matriz.append(lines)

print("Matriz A:")
for i in range(M):
    for j in range(N):
        print(f"{matriz_a[i][j]:4d}", end="")
    print()

print("Matriz B:")
for i in range(N):
    for j in range(P):
        print(f"{matriz_b[i][j]:4d}", end="")
    print()

print("Produto das Matrizes (A x B):")
for i in range(M):
    for j in range(P):
        print(f"{product_matriz[i][j]:4d}", end="")
    print()