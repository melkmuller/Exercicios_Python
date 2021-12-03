# Exercício Python 028: Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar
# descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint
computador = randint(0,5) # Faz o computador sortear aleatóriamente entre 0 e 5
print('==*==' * 20)
print('Pensei num número entre 0 e 5, tente advinhar....')
print('==*==' * 20)
numero = int(input("Em qual número eu pensei? "))
print('Acertouuu!!'if numero == computador else 'Errou!')
print("Pensei no número {}".format(computador))