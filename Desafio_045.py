from random import randint
from time import sleep
print('Vamos jogar Jokenpo!')
itens = ('PEDRA','PAPEL','TESOURA')
computador = randint(0,2)
print('''Suas opções:
[0] PEDRA
[1] PAPEL
[2] TESOURA''')

jogador = int(input('Qual é a sua jogada? '))
print('-=-'*10)

print('JO')
sleep(0.7)
print('KEN')
sleep(0.7)
print('PÔ')
print('-=-'*10)


print(f'Computador jogou {itens[computador]}')
print(f'Jogador jogou {itens[jogador]}')
print('-=-'*10)

if jogador == computador:
    print('EMPATE')

elif computador == 0: #Computador jogou PEDRA
    if jogador == 1:
        print('Jogador venceu!')
    elif jogador == 2:
        print('Computador venceu')
    else:
        print('Jogada inválida!')

elif computador == 1: #Computador jogou PAPEL
    if jogador == 0:
        print('Computador venceu!')
    elif jogador == 2:
        print('Jogador venceu')
    else:
        print('Jogada inválida!')

elif computador == 2: #Computador jogou TESOURA 
    if jogador == 0:
        print('Jogador venceu!')
    elif jogador == 1:
        print('Computador venceu')
    else:
        print('Jogada inválida!')
