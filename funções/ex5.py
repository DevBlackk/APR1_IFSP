"""5) Faça uma função que receba quatro valores reais (faça a consistência), referentes
as notas que um aluno obteve nos bimestres. A função deve retornar a média final desse 
aluno. Pesquise como arredondar a nota"""

def calcular_media(nota_1, nota_2, nota_3, nota_4):
    if 0 <= nota_1 <= 10 and 0 <= nota_2 <= 10 and 0 <= nota_3 <= 10 and 0 <= nota_4 <= 10:
        media = round((nota_1 + nota_2 + nota_3 + nota_4) / 4, 1)
        return media
    else:
        return -1

def main():
    try:
        n1 = float(input("Digite a primeira nota: "))
        n2 = float(input("Digite a segunda nota: "))
        n3 = float(input("Digite a terceira nota: "))
        n4 = float(input("Digite a quarta nota: "))
        
        media = calcular_media(n1, n2, n3, n4)
        
        if media >= 0:
            print(f"Media final: {media:.1f}")
        else:
            print("Erro: as notas devem estar entre 0 e 10!")
        
    except ValueError:
        print("Erro: digite apenas valores numéricos")
    

main()