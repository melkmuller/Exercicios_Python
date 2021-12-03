# Exercício Python 029: Escreva um programa que leia a velocidade de um carro. 
# Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. 
# A multa vai custar R$7,00 por cada Km acima do limite.

vel = int(input("Digite a velocidade do carro: "))
if vel>80:
    print('''O carro está acima do limite de velocidade.
A multa será de R${}'''.format((vel-80)*7))
else:
    print('O carro está dentro do limite de velocidade.')

