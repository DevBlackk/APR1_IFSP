num = int(input("Digite um número: "))
resul = 1
i = 1
while i <= num:
    resul *= i
    print(f"O fatorial de {num}! é: {resul}")
    i += 1