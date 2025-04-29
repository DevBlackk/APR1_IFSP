linhas = 3
colunas = 4
mat = []

for i in range(linhas):
    mat.append([])
    for j in range(colunas):
        x = int(input(f"informe o elemento [{i}][{j}]: "))
        mat[i].append(x)

for i in range(linhas):
    for j in range(colunas):
        print(mat[i][j], end=" ")
    print()

linhas = 3
colunas = 4
mat = []

for i in range(linhas):
    linha = []
    for j in range(colunas):
        x = int(input(f"Informe o elemento [{i}][{j}]: "))
        linha.append(x)
    mat.append(linha)
    print(mat)

for i in range(linhas):
    for j in range(colunas):
        print(mat[i][j], end=" ")
    print()
