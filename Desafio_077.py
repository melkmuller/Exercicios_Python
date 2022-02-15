# Exercício Python 077: Crie um programa que tenha uma tupla com
# várias palavras (não usar acentos). Depois disso, você deve mostrar, para cada palavra, 
# quais são as suas vogais.

palavras = ('ovo','melancia','carros','teste','curso','programacao','database','python','logica')
for p in palavras:
    print(f'Na palavra {p.upper()} temos as vogais: ',end="")
    for l in p:
        if l in "aeiou":
            print(f'{l}', end=" ")
    print('')