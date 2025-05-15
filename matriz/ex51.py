'''1. Crie um programa que solicita do usuário um valor N representando a
quantidade linhas e um valor M representando a quantidade de colunas
de uma matriz. Depois, o programa deverá solicitar do usuário N x M
elementos para serem incluídos na matriz. Por fim, o programa deverá
percorrer a matriz para encontrar e imprimir o seu maior elemento e o
seu menor elemento.'''

M = int(input('Digite a quantidade de linhas: '))
N = int(input('Digite a quantidade de colunas: '))
matriz = []

print("Matriz")
for i in range(M):
    line = []
    for j in range(N):
        value = int(input('Digite os valores da matriz: '))
        line.append(value)
    matriz.append(line)

maior = matriz[0][0]
menor = matriz[0][0]
for i in range(M):
    for j in range(N):
        if matriz[i][j] > maior:
            maior = matriz[i][j]
        if matriz[i][j] < menor:
            menor == matriz[i][j]

print("Matriz:")
for i in range(M):
    for j in range(N):
        print(f'{matriz[i][j]:4d}', end='')
    print()

print(f"Maior elemento: {maior}")
print(f"Maior elemento: {menor}")