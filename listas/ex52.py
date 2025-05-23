'''1. Em geometria analítica, dois vetores podem ser definidos como a=<a1,a2,a3> e
b=<b1,b2,b3>. Escreva um programa que leia dois vetores a e b (duas listas) de
três posições cada e efetue o produto escalar entre eles. O produto escalar é obtido
por ab = a1b1+a2b2+a3b3. De acordo com o exemplo dado abaixo, o calculo a ser
efetuado será: 1x5+4x2+7x3'''

def criar_lista(lista, N):
    i = 0
    print(f"Digite {N} valores inteiros:")
    while i < N:
        num = int(input())
        lista.append(num)
        i += 1

def imprime_lista(lista, N):
    i = 0
    while i < N:
        print(lista[i], end=" ")
        i += 1

def main():
    l1 = []
    l2 = []
    qtde = int(input("Digite o tamanho da lista: "))
    criar_lista(l1, qtde)
    criar_lista(l2, qtde)
    