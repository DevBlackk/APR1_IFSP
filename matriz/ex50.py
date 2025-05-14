'''10. Faça um programa que leia duas matrizes quadradas (A e B) de ordem informada
pelo usuário e verifique se B é a matriz inversa de A. Mostre uma mensagem
amigável ao usuário.'''

N = int(input("Digite a ordem da matirz quadradas: "))
matriz_a = []
matriz_b = []
product = []

print("Digite uma os valores da Matriz A:")
for i in range(N):
    line = []
    for j in range(N):
        value = int(input("Digite um valor da Matriz A: "))
        line.append(value)
    matriz_a.append(line)
print()

print("Digite uma os valores da Matriz A:")
for i in range(N):
    line = []
    for j in range(N):
        value = int(input("Digite um valor da Matriz A: "))
        line.append(value)
    matriz_b.append(line)
print()

for i in range(N):
    line = []
    for j in range(N):
        sumed = 0
        for k in range(N):
            sumed += matriz_a[i][k] * matriz_b[k][j]
        line.append(sumed)
        product.append(line)

is_inverted = True
for i in range(N):
    for j in range(N):
        if i == j and product[i][j] != 1:
            is_inverted = False
        elif i != j and product[i][j] != 0:
            is_inverted = False

if is_inverted:
    print("A matriz B é a inversa da matriz A!")
    print()
else:
    print("A matriz B não é a inversa da matriz A!")
    print()

print("Matriz A:")
for i in range(N):
    for j in range(N):
        print(f"{matriz_a[i][j]:4d}", end="")
    print()

print("Matriz B:")
for i in range(N):
    for j in range(N):
        print(f"{matriz_b[i][j]:4d}", end="")
    print()

print("Produto A x B:")
for i in range(N):
    for j in range(N):
        print(f"{product[i][j]:4d}", end="")
    print()