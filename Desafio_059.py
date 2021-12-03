# Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.

numeros = [0,0]
numeros[0] = float(input('Insira o primeiro valor: '))
numeros[1] = float(input('Insira o segundo valor: '))


menu = int(input('''O que deseja fazer com os números informados?
[ 1 ] Somar
[ 2 ] Multiplicar
[ 3 ] Maior
[ 4 ] Adicionar novos números
[ 5 ] Sair do programa
-------------------------------- '''))

while menu != 5:
    if menu == 1:
        print(f'A soma de {numeros[0]} com {numeros[1]} resulta em: {sum(numeros)}\n')
        input()
    if menu == 2:
        print(f'O multiplicação entre {numeros[0]} e {numeros[1]} resulta em: {numeros[0]*numeros[1]}\n')
        input()
    if menu == 3:
        print(f'O maior número entre {numeros[0]} e {numeros[1]} é o número: {max(numeros)}\n')
        input()
    if menu == 4:
        print('Você decicidu inserir novos valores.')
        numeros[0] = float(input('Insira o primeiro valor: '))
        numeros[1] = float(input('Insira o segundo valor: '))
    if menu not in (1,2,3,4,5):
        print('Opção inválida, escolha novamente!\n5')

    menu = int(input('''O que deseja fazer com os números informados?
[ 1 ] Somar
[ 2 ] Multiplicar
[ 3 ] Maior
[ 4 ] Adicionar novos números
[ 5 ] Sair do programa
--------------------------------: '''))

print('Finalizando programa....')
