# Exercício Python 069: Crie um programa que leia a idade e o sexo de várias pessoas. 
# A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos. 

ficha = dict()
pessoas = list()

while True:
    ficha['idade'] = int(input('Digite a idade da pessoa: '))
    ficha['sexo'] = str(input('Digite o sexo [M ou F]: ')[0].upper())
    pessoas.append(pessoas[:])
    if str(input('Deseja continuar? ')[0].upper()) == 'N':
        break
    