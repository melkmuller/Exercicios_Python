# Exercício Python 063: Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci. 

n = int(input('Quantos termos da Sequência de Fibonacci você deseja ver? '))
t1 = 0
t2 = 1
print(f'{t1} → {t2}', end='')
count = 3
while count <= n:
    t3 = t1 + t2
    print(f' → {t3}', end='')
    t1 = t2
    t2 = t3
    count = count + 1

print(' → FIM')
