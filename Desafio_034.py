# Exercício Python 035: Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

# Entrada de dados
r1 = float(input('Digite o tamanho da primeira reta: '))
r2 = float(input('Digite o tamanho da segunda reta: '))
r3 = float(input('Digite o tamanho da terceira reta: '))

# Analisando os dados
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print(f'As retas {r1}, {r2} e {r3} PODEM formar um TRIÂNGULO')
else:
    print(f'As retas {r1}, {r2} e {r3} NÃO PODEM formar um TRIÂNGULO')
