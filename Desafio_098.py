# Exercício Python 098: Faça um programa que tenha uma função chamada contador(), 
# que receba três parâmetros: início, fim e passo. Seu programa tem que realizar três contagens através da função criada:

# a) de 1 até 10, de 1 em 1
# b) de 10 até 0, de 2 em 2
# c) uma contagem personalizada

def contador(inicio, fim, passo):
    if (inicio > fim and passo > 0) or (inicio < fim and passo <0):
        passo = -passo
    for i in range(inicio, fim+1 if passo > 0 else fim-1, passo): #Esse If inline corrige quando um passo é negativo
        print(f'{i} ', end='')
    print('FIM')

contador(1,10,1)
contador(10, 0, 2)
contador(int(input('Digite o início: ')), int(input('Digite o fim: ')), int(input('Digite o passo: ')))