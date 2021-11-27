# Exercício Python 067: Faça um programa que mostre a tabuada de vários números, 
# um de cada vez, para cada valor digitado pelo usuário.
# O programa será interrompido quando o número solicitado for negativo. 

while True:
    n = int(input('Quer ver a tabuada de qual número? '))
    if n < 0:
        break
    else:
        print(f'''{n} x 1 = {1*n}
{n} x 2 = {2*n}
{n} x 3 = {3*n}
{n} x 4 = {4*n}
{n} x 5 = {5*n}
{n} x 6 = {6*n}
{n} x 7 = {7*n}
{n} x 8 = {8*n}
{n} x 9 = {9*n}
{n} x 10 = {10*n}''')

print('FIM')

    
