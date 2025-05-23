'''3. Elabore a função Real(n) que verifica se o valor de entrada é um número 
real e retorna TRUE em caso afirmativo e FALSE caso contrário.'''

def real(n):
    try:
        n = float(n)
        return True
    except:
        return False

def main():
    numero = input("Digite um número: ")
    if real(numero):
        print(True)
    else:
        print(False)

main()