nota = 0
nota_maiores_igual_6 = 0
nota_maiores_igual_4 = 0
nota_menor_4 = 0
total_notas = 0
while nota >= 0 and nota <= 10:
    nota = float(input("Digite uma nota entre 0 e 10: "))
    if nota >= 6 and nota <= 10:
        nota_maiores_igual_6 += 1
        total_notas += nota
    elif nota >= 4 and nota < 6:
        nota_maiores_igual_4 += 1
        total_notas = total_notas + nota
    elif nota >= 0:
        nota_menor_4 = nota_menor_4 + nota
    else:
        print("Nota inválida")
media = total_notas/(nota_maiores_igual_6 + nota_maiores_igual_4 + nota_menor_4)
print(f"Média das notas: {media:.2f}")
print(f"Total de notas maiores ou igual a 6: {nota_maiores_igual_6}")
print(f"Total de notas maiores ou igual a 4 e menores que 6: {nota_maiores_igual_4}")
print(f"Total de notas manores que 4: {nota_menor_4}")
