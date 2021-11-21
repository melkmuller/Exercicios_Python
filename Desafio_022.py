# Exercício Python 022: Crie um programa que leia o nome completo de uma pessoa e mostre: 
# - O nome com todas as letras maiúsculas e minúsculas.
# - Quantas letras ao todo (sem considerar espaços).
# - Quantas letras tem o primeiro nome.

nome = input("Escreva seu nome completo: ").strip() #Prevenindo espaços antes e depois do nome, para não atrapalhar depois

print(nome.upper()) 
print(nome.lower())
print(len(nome) - nome.count(' ')) #Conta todo o comprimento e subtrai o valor de espaços encontrados

print(nome.find(' ')) #Retorna o número de caracteres até o primeiro espaço, logicamente será a qtde de letras
#Segue abaixo outra forma de fazer

separa = nome.split()
print('Seu primeiro nome tem {} letras'.format(len(separa[0])))