# Exercício Python 053: Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.

frase = input('Digite uma frase: ').upper().replace(' ','')
invertida = ''


# Usando a estrutura de repetição FOR
for c in range(len(frase), 0, -1 ):
    invertida = invertida + frase[c-1]

print(f'A sua frase invertida fica: {invertida}')

if frase == invertida:
    print('A frase é um PALÍNDROMO')

else:
    print('A frase NÃO É um palíndromo')

# Usando um método alternativo, somente com manipulação de String
if frase == frase[::-1]: #Comando que inverte a frase
    print('A frase é um PALÍNDROMO')

else:
    print('A frase NÃO É um palíndromo')