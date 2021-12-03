# Exercício Python 057: Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'.
# Caso esteja errado, peça a digitação novamente até ter um valor correto.

sexo = str(input('Digite o sexo da pessoa [M/F]: ')).upper().strip()

while sexo != 'M' and sexo != 'F':
    sexo = str(input('Dado inválido. Por favor digite a letra M ou F: ')).upper().strip()

if sexo == 'M':
    print('Sexo masculino gravado!')

if sexo == 'F':
    print('Sexo feminino gravado!')