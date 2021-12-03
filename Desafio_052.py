# Exercício Python 052: Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

numero = int(input('Digite um número inteiro: '))
soma = 0

for c in range(1, numero+1, 1):
    if numero % c == 0:
        soma = soma + numero

if soma == soma*2:
    print(f'O número {numero} É PRIMO!')

else:
    print(f'O número {numero} NÃO É primo')
