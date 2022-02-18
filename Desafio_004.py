# Exercício Python 004: Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo
# e todas as informações possíveis sobre ele.

algo = input("Digite algo: ")

print(f'O tipo primitivo desse valor digitado é: {type(algo)}')
print("Só tem espaços? ", algo.isspace())
print("É numérico? ",algo.isnumeric())
print("É alfabético? ",algo.isalpha())

