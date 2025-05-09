valor_cliente = int(input("Digite o valor do lado: "))

if valor_cliente < 100:
  valor_cliente = valor_cliente - (valor_cliente * 0.05)
  print(f"Valor a ser pago com desconte de 5%: {valor_cliente}")
elif valor_cliente > 100 and valor_cliente < 200:
  valor_cliente = valor_cliente - (valor_cliente * 0.10)
  print(f"Valor a ser pago com desconte de 10%: {valor_cliente}")
elif valor_cliente >= 200:
  valor_cliente = valor_cliente - (valor_cliente * 0.20)
  print(f"Valor a ser pago com desconte de 20%: {valor_cliente}")
