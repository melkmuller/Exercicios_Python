# Exercício Python 012: Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

precoAtual = float(input("Digite o valor do produto: R$ "))
print(f'O preço novo, com 5% de desconto é R$ {precoAtual*0.95:.2f}')