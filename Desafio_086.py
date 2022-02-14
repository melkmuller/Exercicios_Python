# Exercício Python 086: Crie um programa que declare uma matriz de dimensão 
# 3x3 e preencha com valores lidos pelo teclado. 
# No final, mostre a matriz na tela, com a formatação correta.

#Primeira forma
# matriz = [[int(input(f'Dgite o número da posição [{j}]-[{i}]: ')) for i in range(3)] for j in range(3)]
# for i in range(3):
#     for j in range(3):
#         print(f'[{matriz[i][j]:^5}]', end='')
#     print()

#Forma enxuta
matriz = [[int(input(f'Dgite o número da posição [{j}]-[{i}]: ')) for i in range(3)] for j in range(3)]
print(f'{matriz[0]}\n{matriz[1]}\n{matriz[2]}')