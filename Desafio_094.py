# Exercício Python 094: Crie um programa que leia nome, sexo e idade de várias pessoas, 
# guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre: 
# A) Quantas pessoas foram cadastradas
# B) A média de idade
# C) Uma lista com as mulheres
# D) Uma lista de pessoas com idade acima da média

galera = list()
pessoa = dict()
soma = 0

#Entrada de dados e validações
while True:
    pessoa.clear() #Limpa o dicionário da pessoa antes de iniciar um cadastro
    pessoa['nome'] = str(input("Nome: "))

    # Enquanto usuário não digitar M ou F ele fica no loop, saindo somente com uma resposta válida
    while True:
        pessoa['sexo'] = str(input("Sexo (M/F):")).upper()[0] #Joga tudo para maiúsculo e pesga somente o carctere na posição 0, o primeiro.
        if pessoa['sexo'] in 'MF':
            break
        print("ERRO! Por favor, digite somente M ou F")
    pessoa['idade'] = int(input("Idade: "))
    galera.append(pessoa.copy()) #Faz uma cópia do dicionário e joga na lista 'galera'
    soma += pessoa['idade']

    # Enquanto usuário não digitar S ele fica no loop, ou se digitar algo diferente de S ou N fica num sub loop
    while True:
        resp = str(input("Quer continuar (S/N)? :")).upper()[0]
        if resp in 'SN':
            break #Sai do sub loop somente quando usuário digita alguma resposta válida
        print("ERRO! Por favor digite somente S ou N.")
    if resp == 'N':
        break #Sai do loop somente quando o usuário digita N, que quer continuar

#Saída de dados
print()
print(f'A) Ao todos temos {len(galera)} pessoas cadastradas')
print(f'B) A média de idade é {soma / len(galera):5.2f}')
print('C) As mulheres cadastradas foram: | ', end='')
for pessoa in galera:
    if pessoa['sexo'] == 'F':
        print(f' {pessoa["nome"]}', end=' |')
print()
print(f'D) Lista das pessoas que estão acima da média de idade: ', end='')
for p in galera:
    if p['idade'] > (soma / len(galera)):
        print()
        for chave, valor in p.items():
            print(f'[{chave} = {valor}] ', end='')
        print()  