# Exercício Python 016: Crie um programa que leia um número Real qualquer pelo 
# teclado e mostre na tela a sua porção Inteira.

from math import trunc

numero = float(input('Digite um valor: '))
print(f'O valor digitado foi {numero} e sua porção inteira é {trunc(numero)}')