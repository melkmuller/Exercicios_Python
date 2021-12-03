# Exercício Python 049: Mostre a tabuada de um número que o usuário escolher, utilizando um laço for.

numero = int(input('Digite o número do qual deseja ver a tabuada: '))
contador = int(input('Deseja ver a tabuada até qual número? '))

for contador in range(1, contador+1 , 1):
    print(f'{numero} x {contador}: {contador*numero}')