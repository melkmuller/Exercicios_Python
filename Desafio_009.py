# Exercício Python 009: Faça um programa que leia um número Inteiro 
# qualquer e mostre na tela a sua tabuada.

numero = int(input("Digite um número para ver sua tabuada: "))
for i in range(10):
    print(f'{numero} X {i+1}: {(i+1)*numero}')