print('Exercício Python 55: Faça um programa que leio o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lido.')

lista_pesos = [];

for c in range(1,6,1):
    peso = float(input(f'Informe o peso da {c}ª pessoa: '))
    lista_pesos += [peso]

print(f'O maior peso é de {max(lista_pesos)} Kg')
print(f'O menor peso é de {min(lista_pesos)} Kg')