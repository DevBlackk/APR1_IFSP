'''8. Dada uma string com uma frase informada pelo usuário (incluindo
espaços em branco), conte a quantidade de espaços em branco e a
quantidade de vezes que aparecem as vogais a, e, i, o, u.'''

phrase = input("Digite uma frase: ")
vogais = 'aeiouAEIOU'
count_vogais = 0
count_spaces = 0
i = 0
while i < len(phrase):
    if phrase[i] == ' ':
        count_spaces += 1
    elif phrase[i] in vogais:
        count_vogais += 1
    i += 1

print(f"Quantidade de vogais: {count_vogais}")
print(f"Quantidade de espaços: {count_spaces}")