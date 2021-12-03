# Exercício Python 066: Crie um programa que leia números inteiros pelo teclado. 
# O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. 
# No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).


numero = soma = contador  = 0 

print('Digite o número 999 para o programa finalizar!')
while True:
    numero = (float(input('Insira um número: ')))
    if numero == 999:
        break
    contador += 1
    soma += numero
print(f'Foram digitados {contador} e a soma de todos é {soma}')