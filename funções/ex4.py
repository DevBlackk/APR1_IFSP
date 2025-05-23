'''4. Crie uma função que receba como parâmetro um número inteiro. A função deve 
retornar um número inteiro, conforme a seguir:
1. Retornar 1 se o número recebido é positivo
2. Retornar -1 se o número recebido é negativo
3. Retornar 0 se o número recebido é zero'''

def verificador_de_numero(n):
    if n > 0:
        return 1
    elif n == 0:
        return 0
    else:
        return -1

def main():
    numero = int(input("Digite um número: "))
    verificador = verificador_de_numero(numero)
    if verificador == 1:
        print("É um número positivo")
    elif verificador == -1:
        print("É um inteiro negativo!")
    else:
        print("É zero!")

main()