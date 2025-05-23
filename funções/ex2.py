'''2. Elabore a função Inteiro(n) que verifica se o valor de entrada é um
número inteiro e retorna Verdadeiro em caso afirmativo e Falso caso contrário.'''

def inteiro(n):
    try:
        n = int(n)
        return True
    except: 
        False

def main():
    numero = input("Digite um número: ")
    if inteiro(numero):
        print(True)
    else:
        print(False)

main()
