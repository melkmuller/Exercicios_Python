# Exercício Python 051: Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

print('='*40)
print('{:^40}'.format( '10 TERMOS DE UMA PA '))
print('='*40)

inicio = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a Razão: '))

for c in range (inicio, razao*10, razao):
    print(f' {c} → ', end="")

print('FIM')