# Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.

dados = list()
pessoas = list()
maior = menor = 0
while True:
    dados.append(str(input("Digite o nome: ")))
    dados.append(int(input("Digite o peso: ")))

    if len(pessoas) == 0:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]

    pessoas.append(dados[:])
    dados.clear()
    verificador = str(input("Deseja adicionar mais uma pessoa? S/N: ")).strip().upper()
    if verificador != "S":
        break

print(f'Foram adicionados um total de {len(pessoas)} pessoas')
print(f'O maior peso foi de {maior}Kg. Peso de ', end=" ")
for p in pessoas:
    if p[1]==maior:
        print(f'[{p[0]}]', end='')
print()
print(f'O menor peso foi de {menor}Kg. Peso de ', end=" ")
for p in pessoas:
    if p[1]==menor:
        print(f'[{p[0]}]', end='')
 