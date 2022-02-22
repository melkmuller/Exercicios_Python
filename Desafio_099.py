# Exercício Python 099: Faça um programa que tenha uma função chamada maior(), 
# que receba vários parâmetros com valores inteiros. Seu programa tem que analisar 
# todos os valores e dizer qual deles é o maior.

def maior(*valores):
    print(f'Analisando os valores informados: {valores}')
    print(f'Foram informados ao todo {len(valores)} valores')
    print(f'O maior valor informado foi: {max(valores)}')
    print(f'*'* 50)

maior(5,7,9,12,145,6)
maior(2,1)
maior(88,45,23,47,25,26,35,665)
maior(8568,24568,24893,256332,244887,20360)