# Exercício Python 058: Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10. 
# Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

from random import randint

print('''Olá! Eu sou o computador....
Acabei de pensar em um número entre 0 e 10.
Em quantos palpites você consegue advinhar qual é o número?''')

computador = randint (0,10)
jogador = int(input('Qual é o seu palpite?... '))
contador = 1

while jogador != computador:
    if computador < jogador:
        jogador = int(input('Menos... Tente mais uma vez: '))
    else:
        jogador = int(input('Mais... Tente mais uma vez: '))
    contador += 1

print(f'Parabéns você acertou com {contador} tentativa(s)')
