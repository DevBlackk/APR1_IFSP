'''9. Um anagrama é uma palavra que é feita a partir da transposição das
letras de outra palavra ou frase. Por exemplo, “Iracema” é um
anagrama para “America”. Escreva um programa que decida se uma
string é um anagrama de outra string, ignorando os espaços em branco.
O programa deve considerar maiúsculas e minúsculas como sendo
caracteres iguais, ou seja, “a” = “A”.'''

str_1 = input("Digite uma frase: ")
str_2 = input("Digite outra frase: ")

str_1 = str_1.lower().replace(' ', '')
str_2 = str_2.lower().replace(' ', '')

if len(str_1) == len(str_2):
    anagrama = True
    i = 0
    while i < len(str_1):
        count_str_1 = 0
        count_str_2 = 0
        for j in range(len(str_1)):
            if str_1[j] == str_1[i]:
                count_str_1 += 1
        j = 0
        while j < len(str_2):
            if str_1[i] == str_2[j]:
                count_str_2 += 1
            j += 1
        i += 1
        if count_str_1 != count_str_2:
            anagrama = False
    if anagrama:
        print("É um anagrama!")
    else:
        print("Não é um anagrama!")