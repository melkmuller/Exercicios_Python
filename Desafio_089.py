# Exercício Python 089: Crie um programa que leia nome e duas notas de vários alunos e
# guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de 
# cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.

ficha = []

while True:
    nome = str(input("Nome: "))
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    media = (nota1+nota2)/2
    ficha.append([nome, [nota1, nota2], media])
    verificador = str(input("Quer continuar? (S/N): ")).upper().strip()
    if verificador != 'S':
        break

print(f'{"Cód.":<4}{"Nome":>15}{"Média":>8}')

for indice,aluno in enumerate(ficha):
    print(f'{indice:<4}{aluno[0]:>15}{aluno[2]:>8}')

while True:
    codigo = int(input("Mostrar notas de qual aluno? (cód. 999 interrompe): "))
    if codigo == 999:
        break
    if codigo  <= len(ficha)-1:   
        print(f'Notas de {ficha[codigo][0]}: {ficha[codigo][1]}')