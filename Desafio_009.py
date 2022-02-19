# Exercício Python 009: Faça um programa que leia um 
# número Inteiro qualquer e mostre na tela a sua tabuada.

num = int(input("Digite o número: "))

for i in range(10):
    print(f'{i+1} * {num} = {(i+1) * num}')
