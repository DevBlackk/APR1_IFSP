for numero1 in range(1, 11):
  for numero2 in range(1, 11):
    resultado = numero1 * numero2
    print(f"{numero1} x {numero2} = {resultado}")
print()

## Refataroção com while

i = 0
while i <= 10:
  j = 0
  while j <= 10:
    resultado = i * j
    print(f"{i} x {j} = {resultado}") 
    j = j + 1
  i = i + 1