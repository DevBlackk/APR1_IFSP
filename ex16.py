numero = int(input("Digite um número: "))

if numero <= 1:
  print("Número invalido!")
else:
  flag = False
  i = 2
  while i <= numero // 2 + 1:
    validator = numero % i
    print(validator, i)
    if validator == 0:
      flag = True
    i = i + 1
  if flag:
    print("Não primo")
  else:
    print("Primo")