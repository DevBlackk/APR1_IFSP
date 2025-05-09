numero = int(input("Digite um número: "))
print(f"Tabuada do {numero}: ")
for i in range(1, 11):
  resultado = numero * i
  print(f"{numero} x {i} = {resultado}")

## refatoração em while
numero = int(input("Digite um número: "))
i = 0
while i <= 10:
  resultado = numero * i
  print(f"{numero} x {i} = {resultado}")
  i = i + 1