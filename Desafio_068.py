# Exercício Python 068: Faça um programa que jogue par ou ímpar com o computador. 
# O jogo só será interrompido quando o jogador perder, 
# mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

from random import randint
from time import sleep
contador = 0

while True:
    n = int(input('Qual número você joga? '))
    pi = str(input('Par ou Ímpar? [P/I]')).strip().upper()
    print('=*20')

    computador = randint(0,10)
    print('PAR')
    sleep(0.7)
    print('OU')
    sleep(0.7)
    print('ÍM')
    sleep(0.7)
    print('PAR')
    
    resultado = ''
    if ((n + computador) %2 == 0):
        resultado = 'PAR'
    else:
        resultado = 'ÍMPAR'

    if resultado == 'PAR' and pi == 'P':
        quem_venceu = 'VOCÊ VENCEU'
    else:
        quem_venceu = 'COMPUTADOR VENCEU'

    print(f'Você jogou {n} e o computador jogou {computador}. O total foi {n+computador}, deu {resultado}, {quem_venceu}')

    if quem_venceu == 'VOCÊ VENCEU':
        contador += 1
        print(f'Vamos jogar novamente, você já venceu {contador} vezes')
    else:
        print(f'O jogo acabou. Você ganhou {contador} vezes')
        break