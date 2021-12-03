print('''Exercício Python 056: Desenvolva um programa que leia o nome, idade e sexo de quatro pessoas.
No final, mostre: a média de idade do grupo, qual o nome do homem mais velho e quantas mulheres têm menos de 20 anos''')

lista_idades = []
lista_nomes_homens = ['Não há nenhum homem']
lista_idades_masc = [0]
total_idade = 0
menores20 = 0
for contador in range(1, 5, 1):
    print('{:*^40}'.format( f' {contador}ª PESSOA '))
    nome = str(input('Informe o nome da pessoa: '))
    idade = int(input('Informe a idade da pessoa: '))
    lista_idades.append(idade)
    total_idade += idade
    sexo = input('Informe o sexo [M/F]: ').upper().strip()
    if sexo == 'M':
        lista_idades_masc.append(idade)    
        lista_nomes_homens.append(nome)    
    if sexo == 'F' and idade < 20:
        menores20 += +1
print(f'A média de idade do grupo é de {total_idade/4} anos')
print('Nome do homem mais velho: {}.'.format(lista_nomes_homens[lista_idades_masc.index(max(lista_idades_masc))]))
print(f'{menores20} é o total de mulheres menores de 20 anos')