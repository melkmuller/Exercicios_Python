#  Exercício Python 043: Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status
# - IMC abaixo de 18,5: Abaixo do Peso
# - Entre 18,5 e 25: Peso Ideal
# - 25 até 30: Sobrepeso
# - 30 até 40: Obesidade
# - Acima de 40: Obesidade Mórbida

#Entrada de dados
peso = float(input('Digte o peso da pessoa em Kg: '))
altura = float(input('Digite a altura de pessoa em Metros: '))

#Processamento de dados
imc = peso / (altura*altura)

#Saída de dodos
if imc < 18.5:
    print(f'O IMC é de {imc:.1f}, pessoa Abaixo do Peso Ideal, IMC abaixo de 18.5')
elif imc >= 18.5 and imc <= 25:
    print(f'O IMC é de {imc:.1f}, pessoa está no Peso Ideal, IMC entre 18.5 e 25')
elif imc > 25 and imc <=30:
    print(f'O IMC é de {imc:.1f}, pessoa está com Sobrepeso, IMC entre 25 e 30')
elif imc > 30 and imc <=40:
    print(f'O IMC é de {imc:.1f}, pessoa em Obesidade, IMC entre 30 e 40')
else:
    print(f'O IMC é de {imc:.1f}, pessoa em Obesidade Mórbida, IMC acima de 40')
