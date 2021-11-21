# Exercício Python 027: Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

nome = input("Digite seu nome completo: ").title().split()
print('Seu primeiro nome é: {}'.format(nome[0]))
print('Seu último nome é: {}'.format(nome[-1])) # A pisção (-1) pega a última posição da lista, (-2) pega a penúltima e assim por diante
