a = float(input("Digite o valor do lado A: "))
b = float(input("Digite o valor do lado B: "))
c = float(input("Digite o valor do lado C: "))

if a < b + c and b < a + c and c < a + b:
  if a == b == c:
    print("É um triângulo equilátero.")
  elif a == b or a == c or b == c:
    print("É um triângulo isósceles.")
  else:
    print("É um triângulo escaleno.")
else:
  print("Os valores fornecidos não formam um triângulo.")
