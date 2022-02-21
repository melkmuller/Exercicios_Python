# Exercício Python 090: Faça um programa que leia nome e média de um aluno, 
# guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.

from statistics import median


ficha = dict()

ficha['nome'] = str(input("Digite o nome do aluno: "))
ficha['media'] = float(input("Digite a média do aluno: "))
ficha['situacao'] = 'Aprovado' if ficha['media'] >= 7 else 'Reprovado' if ficha['media'] < 6 else 'Recuperacao'

for key, value in ficha.items():
    print(f'{key} é {value} ')