# Exercício Python 092: Crie um programa que leia nome, ano de nascimento e carteira de trabalho e 
# cadastre-o (com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário 
# receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, 
# com quantos anos a pessoa vai se aposentar.

from datetime import datetime
ficha = dict()

ficha['nome'] = str(input("Nome: "))
ficha['idade'] = datetime.now().year - int(input("Ano de nascimento: ")) 
ficha['ctps'] = int(input("Nº da Carteira de trabalho (0 para 'não tem'): "))

if ficha['ctps'] == 0:
    for chave, valor in ficha.items():
        print(f'    - {chave}: {valor}')
else:
    ficha['anoContratacao'] = int(input("Ano de contratação: "))
    ficha['salário'] = float(input("Salário: "))
    ficha['aposentadoria'] = ficha['idade'] + ((ficha['anoContratacao'] + 35) - datetime.now().year)
    for chave, valor in ficha.items():
        print(f'    - {chave}: {valor}')