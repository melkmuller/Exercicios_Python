# Exercício Python 010: Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e 
# mostre quantos dólares ela pode comprar.

valor = float(input("Quanto dinheiro você tem na carteira? R$ "))
print(f'Você consegue comprar U$ {(valor / 5.52).2f}')