# Exercício Python 050: Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.

soma = 0
for contador in range(0, 6, 1):
    num = float(input("Digite um número: "))
    if num %2 == 0:
        soma += num
print(f'A soma dos números PARES digitados é {soma}')
