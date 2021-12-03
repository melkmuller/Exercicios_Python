# Exercício Python 048: Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três e que se encontram no intervalo de 1 até 500.

soma = 0
for numero in range(1, 501, 2):
    if numero % 3 == 0 and numero % 2 != 0:
        soma = soma + numero
print(soma)