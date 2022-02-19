# Exercício Python 018: Faça um programa que leia um ângulo qualquer e 
# mostre na tela o valor do seno, cosseno e tangente desse ângulo.

import math

angulo = float(input('Digite o valor do ângulo: '))
print(f'Seno: {math.sin(math.radians(angulo)):.2f}') # Transforma o ângulo de Graus para Radiano e depois pega o Seno
print(f'Cosseno: {math.cos(math.radians(angulo)):.2f}')
print(f'Tangente: {math.tan(math.radians(angulo)):.2f}')