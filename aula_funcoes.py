num_1 = int(input("Digite um número: "))
num_2 = int(input("Digite outro número: "))

def soma(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplica(a, b):
    return a * b


def dividi(a, b):
    return a / b


result_soma = soma(num_1, num_2)
result_subtrair = subtrair(num_1, num_2)
result_diviir = dividi(num_1, num_2)
result_multiplicar = multiplica(num_1, num_2)

print(f"O resuntado do é: {result_soma, result_subtrair, result_multiplicar, result_diviir}")