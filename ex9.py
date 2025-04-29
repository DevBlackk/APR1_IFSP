num1 = int(input("Digite o primeiro numero: "))
num2 = int(input("Digite o segundo numero: "))
num3 = int(input("Digite o terceiro numero: "))

if num1 > num2:
  num1, num2 = num2, num1
if num1 > num3:
  num1, num3 = num3, num1
if num2 > num3:
  num2, num3 = num3, num2

print(f"A ordem crescente é: {num1}, {num2}, {num3}")