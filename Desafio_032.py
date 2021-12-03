# Exercício Python 032: Faça um programa que leia um ano qualquer e mostre se ele é bissexto.

from datetime import date

ano = int(input('Digite o ano que deseja avaliar. Digite 0 para o ano atual: '))

if ano == 0:
    ano = date.today().year #Pega o ano atual da máquina do usuário
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0: #Faz todas as verificações de um ano bissexto
    print('O ano {} é BISSEXTO!'.format(ano))
else:
    print('O ano {} NÃO É BISSEXTO!'.format(ano))