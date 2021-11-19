# Exercício Python 006: Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

n = int(input("Digite um número inteiro: "))
print("Analisando o valor digitado....\nO dobro é {}\nO triplo é {}\nA raiz quadrada é {:.4f}".format((n*2),(n*3),(n**(1/2))))