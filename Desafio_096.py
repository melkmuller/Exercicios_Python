# Exercício Python 096: Faça um programa que tenha uma função chamada área(),
# que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.

def área(largura, comprimento):
    print(f'A área é de: {largura*comprimento}m²')

l = float(input('Informe a largura do terreno (m): '))
c = float(input('Informe o comprimento do terren0 (m): '))
área(l,c)