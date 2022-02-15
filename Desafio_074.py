# Exercício Python 074: Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. 
# Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor
# que estão na tupla.

from random import sample
from random import randint

# numeros = tuple(sample(range(10),5)) #Primeira forma de fazer 
numeros = tuple(randint(1,10) for i in range (5))


print(f'Os valores sorteados foram: {numeros}')
print(f'\nO maior valor sortado foi: {max(numeros)}')
print(f'O menor valor sorteado foi: {min(numeros)}')