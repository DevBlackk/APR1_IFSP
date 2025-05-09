nota_1 = float(input("Digite uma nota: "))
nota_2 = float(input("Digite outro nota: "))

peso_1 = 6
peso_2 = 4
media_ponderada = (nota_1 * peso_1 + nota_2 * peso_2) / peso_1 + peso_2

print(f"A média ponderada é: {media_ponderada:.1f}")