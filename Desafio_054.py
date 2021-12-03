from datetime import date, datetime

print('Exercício Python 054: Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.\n')

menores = 0
maiores = 0

for c in range(1, 8, 1):
    ano = int(input(f'Informe o ano de nascimento da {c}ª pessoa: '))

    if datetime.today().year - ano < 18:
        menores = menores+1
    
    else:
        maiores = maiores+1

print(f'''Ao todo são:
{maiores} pessoas MAIORES de idade
{menores} pessoas MENORES de idade''')
