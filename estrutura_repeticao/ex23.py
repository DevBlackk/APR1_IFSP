list_multiples_than_3 = []
i = 0

while i <= 150:
    if i % 3 == 0:
        list_multiples_than_3.append(i)
    i += 1

print(f"Os números múltiplos de 3 entre 0 e 150 são: {list_multiples_than_3}")