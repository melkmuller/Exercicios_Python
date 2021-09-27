# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
#             – Até 9 anos: MIRIM
#            – Até 14 anos: INFANTIL
#           – Até 19 anos: JÚNIOR
#          – Até 25 anos: SÊNIOR
#         – Acima de 25 anos: MASTER

ano_nascimento = int(input("Informe a data de nascimento do atleta: \n")) #Recebe o valor digitado pelo usuário
from datetime import date
ano_atual = date.today().year #Puxa da data, somente o ANO de hoje

if((ano_atual - ano_nascimento) > 0 and (ano_atual - ano_nascimento) <= 9):
    print("MIRIM\n")

elif((ano_atual - ano_nascimento) > 9 and (ano_atual - ano_nascimento) <= 14):
    print("INFANTIL\n")

elif((ano_atual - ano_nascimento) > 14 and (ano_atual - ano_nascimento) <= 19):
    print("JÚNIOR\n")

elif((ano_atual - ano_nascimento) > 19 and (ano_atual - ano_nascimento) <= 25):
    print("SÊNIOR\n")

else:
    print("MASTER\n")