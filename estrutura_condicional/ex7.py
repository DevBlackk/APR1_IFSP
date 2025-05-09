num1 = int(input("Digite o primeiro numero: "))
num2 = int(input("Digite o segundo numero: "))
num3 = int(input("Digite o terceiro numero: "))
num4 = int(input("Digite o quarto numero: "))
num5 = int(input("Digite o quinto numero: "))

maior_numero = num1
if num2 > maior_numero:
  maior_numero = num2
if num3 > maior_numero:
  maior_numero = num3
if num4 > maior_numero:
  maior_numero = num4
if num5 > maior_numero:
  maior_numero = num5

print(f"O maior numero digitado foi: {maior_numero}")
