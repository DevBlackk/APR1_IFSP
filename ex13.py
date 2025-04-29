for numero in range(1, 100):
  if numero % 7 == 0 and numero % 3 == 0:
    print(f"O número {numero} é divisível por 7 e 3")

## Refatoração em while
i = 1
while i <= 100:
  if i % 7 == 0 and i % 3 == 0:
    print(f"O número {i} é divisivel por 7 e 3")
  i = i + 1