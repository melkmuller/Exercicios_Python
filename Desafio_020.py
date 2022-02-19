# Exercício Python 020: O mesmo professor do desafio 019 quer sortear a ordem de apresentação de trabalhos dos alunos. 
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

from random import sample

#Cria uma lista para receber os alunos
alunos = list()
for i in range(4):# Roda um for para adicionar quatro alunos na lista
    alunos.append(input("Digite o nome do aluno: "))
print(f'A ordem de apresentação é: {sample(alunos, 4)}')#Randomiza e ordem através da ferramenta Sample