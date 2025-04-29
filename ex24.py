N = int(input("Digite o número de alunos: "))
grade_list = []
average = 0
i = 0

while i < N:
    grade = int(input("Digite a nota do aluno de 1 a 10: "))
    if grade < 0 or grade > 10:
        print("Nota inválida. Digite novamente.")
        continue
    
    grade_list.append(grade)
    i += 1

j = 0
while j < len(grade_list):
    average += grade_list[j]
    j += 1

print(f"Ás notas dos alunos foi: {grade_list}")
print(f"A média é: {average / N:.1f}")