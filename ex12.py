for numero in range(1, 100):
  if numero % 7 == 0:
    print(f"O número {numero} é divisível por 7")

## Refatoração com while
i = 0
while i <= 100:
  if i % 7 == 0:
    print(f"O número {i} é divisível por 7")
  i = i + 1