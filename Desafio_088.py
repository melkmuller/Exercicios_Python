# Exercício Python 088: Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
# O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo,
# cadastrando tudo em uma lista composta.

# from random import randint

# contador = int(input("Quantos jogos você quer que eu sorteie? "))
# apostas = []
# lista = []
# contadorNumeros = 0

# for c in range(contador):
#     while True:
#         numero = randint(1,60)
#         if numero not in lista:
#             lista.append(numero)
#             contadorNumeros += 1
#         if contadorNumeros >= 6:
#             apostas.append(lista[:])
#             lista.clear()
#             contadorNumeros = 0
#             break

# for c in range(contador):
#     print(f'Jogo {c+1}: {sorted(apostas[c])}')

# Forma otimizada
# Sample gera números aleaórios não repetidos
from random import sample

quantidadeApostas = int(input("Quantas apostas quer gerar? "))
numeros = [sample(range(1,61), k=6) for x in range(quantidadeApostas)] 

for jogo in range(quantidadeApostas):
    print(f'Jogo {jogo+1}: {sorted(numeros[jogo])}')