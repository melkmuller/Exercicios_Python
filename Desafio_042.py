# Exercício Python 042: Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# - EQUILÁTERO: todos os lados iguais
# - ISÓSCELES: dois lados iguais, um diferente
# - ESCALENO: todos os lados diferentes

print('Vamos analisar um triângulo!')

#Entrada de dados
r1 = float(input('Digite o tamanho da primeira reta: '))
r2 = float(input('Digite o tamanho da segunda reta: '))
r3 = float(input('Digite o tamanho da terceira reta: '))

#Processamento de dados e saída
if r1 == r2 and r2 == r3:
    print(f'As retas {r1}, {r2} e {r3} formam um triângulo EQUILÁTERO')

elif r1 == r2 and r1 != r3 or r1 == r3 and r1 != r2:
    print(f'As retas {r1}, {r2} e {r3} formam um triângulo ISÓSCELES')
    
else:
    print(f'As retas {r1}, {r2} e {r3} formam um triângulo ESCALENO')