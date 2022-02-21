# Exercício Python 030: Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

#Entrada de dados
numero = float(input("Digite um número: "))

#Processamento
if numero % 2 == 0:
    print(f'O número {numero} é PAR!')
else:
    print(f'O número {numero} é ÍMPAR!')