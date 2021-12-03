# Exercício Python 065: Crie um programa que leia vários números inteiros pelo teclado. 
# No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

lista_num = []
lista_num.append(float(input('Digite um valor númérico: ')))
check = str(input('Deseja continuar? [S / N]')).strip().upper()
while check != 'N':
    lista_num.append(float(input('Digite mais um valor númérico: ')))
    check = str(input('Deseja continuar? [S / N]')).strip().upper()

print(f'A média de todos os valores digitados é {sum(lista_num)/len(lista_num)}.')
print(f'O maior valor digitado é o número {max(lista_num)}.')
print(f'O menor valor digitado é o número {min(lista_num)}.')