# Exercício Python 025: Crie um programa que leia o nome de uma pessoa e diga se ela tem "Silva" no nome.

nome = input('Digite seu nome completo: ').title()
print('Seu nome tem Silva? {}'.format('Silva' in nome.split()))