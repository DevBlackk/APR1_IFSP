i = 1
soma = 0
n = int(input("Digite n: "))
m = 1
print(f"S = ", end="")

while i < n + 1:
    print(f"{i}/{m}", end="")
    if i < n:
        print(" + ", end="")
    else:
        print()
    soma += i / m
    i += 1
    m += 2

print(f"A soma da série deu {soma:.2f}")