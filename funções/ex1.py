'''1. Elabore a função InteiroPositivo(n) que verifica se o valor de entrada é um 
número inteiro positivo e retorna Verdadeiro em caso afirmativo e Falso caso contrário.'''

def inteiro_positivo(numero):
    try:
        numero = int(numero)
        if numero >= 0:
            return True
        else:
            return False
    except:
        return False

def main():
    num = input("Digite um número: ")
    if inteiro_positivo(num):
        print("É um inteiro positivo!")
    else:
        print("Não é um inteiro positivo!")

main()