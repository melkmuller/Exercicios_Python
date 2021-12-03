# Exercício Python 033: Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

v1 = float(input('Digite o primeiro valor: '))
v2 = float(input('Digite o segundo valor: '))
v3 = float(input('Digite o terceiro valor: '))
numeros = [v1,v2,v3]

print(f'O menor número é {(min(numeros))}')
print(f'O maior número é {(max(numeros))}')
