print("Calculadora")

def fun_soma():
    n1 = float(input("Digite o primeiro número: "))
    n2 = float(input("Digite o segundo número: "))
    print(f"Resultado: {n1 + n2}")

def fun_subtrair():
    n1 = float(input("Digite o primeiro número: "))
    n2 = float(input("Digite o segundo número: "))
    print(f"Resultado: {n1 - n2}")

def fun_multiplicar():
    n1 = float(input("Digite o primeiro número: "))
    n2 = float(input("Digite o segundo número: "))
    print(f"Resultado: {n1 * n2}")

def fun_dividir():
    n1 = float(input("Digite o primeiro número: "))
    n2 = float(input("Digite o segundo número: "))
    if n2 != 0:
        print(f"Resultado: {n1 / n2}")
    else:
        print("Erro: Divisão por zero!")

def main():
    opcao = 1
    while opcao != 0:
        print("\nEscolha a operação:")
        print("1. Adição")
        print("2. Subtração")
        print("3. Multiplicação")
        print("4. Divisão")
        print("0. Sair")
        
        opcao = int(input("Escolha uma opção: "))

        match opcao:
            case 1: 
                fun_soma()
            case 2:
                fun_subtrair()
            case 3:
                fun_multiplicar()
            case 4:
                fun_dividir()
            case 0:
                print("Programa encerrado!")
            case _:
                print("Opção inválida!")

main()