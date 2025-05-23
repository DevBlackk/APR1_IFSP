"""6) Faça uma função que receba quatro valores, referentes as notas que um aluno obteve
nos bimestres. A função deve retornar Verdadeiro se o aluno foi aprovado e Falso caso 
contrário. """

def calcular_media(n1, n2, n3, n4, n5):
    if 0 <= n1 <= 10 and 0 <= n2 <= 10 and 0 <= n3 <= 10 and 0 <= n4 <= 10 and 0 <= n5 <= 10:
        media = round((n1 + n2 + n3 + n4 + n5) / 4, 1)
        return media
    else:
        return -1

def passou_ou_nao(validador):
    if validador >= 5 and validador <= 10:
        return True
    else:
        return False

def main():
    nota_1 = float(input("Digite a primeira nota: "))
    nota_2 = float(input("Digite a segunda nota: "))
    nota_3 = float(input("Digite a terceira nota: "))
    nota_4 = float(input("Digite a quarta nota: "))
    nota_5 = float(input("Digite a quinta nota: "))
    
    media_final = calcular_media(nota_1, nota_2, nota_3, nota_4, nota_5)
    
    if passou_ou_nao(media_final):
        print("Passou de ano!")
        print(f"A sua média foi {media_final}")
    else:
        print("Não passou de ano!")

main()
