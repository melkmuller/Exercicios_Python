# Exercício Python 024: Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "Santo".

cidade = input("Digite o nome da cidade: ")

# Método 01
# cidade = cidade.split()
# cidade = cidade.capitalize()
# print('Santo' in cidade[0])

# Método 02
print(cidade[:5].capitalize() == 'Santo')
