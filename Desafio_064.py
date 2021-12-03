# Exercício Python 064: Crie um programa que leia vários números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. 
# No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).

print('''Vamos somar todos o números que você digitar.
Para finalizar digite 999''')

flag = 0
soma = 0
contador = 0

while flag != 999:
    n = int(input('Insira um número inteiro: '))
    flag = n
    if(n != 999):
        soma += n
        contador += 1

print(f'A soma de todos os {contador} números digitados é {soma}')


    