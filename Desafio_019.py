# Exercício Python 019: Um professor quer sortear um dos seus quatro alunos para apagar o quadro. 
# Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido. 

from random import sample

#Cria uma lista para receber os alunos
alunos = list()
for i in range(4):# Roda um for para adicionar quatro alunos na lista
    alunos.append(input("Digite o nome do aluno: "))
print(f'O aluno sorteado é: {sample(alunos, 1)}')#Escolhe um através da ferramenta Sample