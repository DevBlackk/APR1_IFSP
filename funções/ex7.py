"""7) Faça uma função que calcule o fatorial de um número inteiro positivo (faça a 
consistência). Transforme seus programas de consistência de número já implementados para 
funções."""

def inteiro_positivo(n):
    n = int(n)
    if n >= 0:
        return True
    else:
        return False

def calculo_fatorial(n):
    if inteiro_positivo(n) == False:
        return -1

    fatorial = 1
    for i in range(1, n + 1):
        fatorial *= i
    return fatorial

def main():
    num = int(input("Digite um númeor: "))
    
    resultado = calculo_fatorial(num)
    
    if resultado >= 0:
        print(f"O fatorial de {num} é {resultado}")
    else:
        print("Erro: Digite apenas numeros inteiros positivos!")

main()