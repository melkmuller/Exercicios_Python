# Exercício Python 100: Faça um programa que tenha uma lista chamada números e duas funções 
# chamadas sorteia() e somaPar(). A primeira função vai sortear 5 números e vai colocá-los 
# dentro da lista e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.

from random import randint

def sorteia():
    numeros = [randint(1,101) for i in range (5)]
    print(f'Os números sorteados foram {numeros}')
    return numeros


def somaPar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'A soma dos números pares é {soma}')

somaPar(sorteia())