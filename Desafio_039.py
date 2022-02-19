# Exercício Python 039: Faça um programa que leia o ano de nascimento de um jovem e informe, 
# de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. 
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date
#Entrada de dados
ano_nascimento = int(input('Informe seu ano de nascimento: '))

if (date.today().year) - ano_nascimento == 18:
    print('Você completa 18 anos neste ano, precisa se alistar')
if (date.today().year) - ano_nascimento < 18:
    print(f'Falta(m) {18 - ((date.today().year) - ano_nascimento)} ano(s) para você se alistar')
if (date.today().year) - ano_nascimento > 18:
    print(f'Você já deveria ter se alistado, está {((date.today().year) - ano_nascimento) - 18} ano(s) atrasado')
