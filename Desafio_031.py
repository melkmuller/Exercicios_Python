# Exercício Python 031: Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, 
# cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

#Entrada de dados
distancia = int(input('Qual a distância da viagem? '))

#Proessamento de dados
if distancia <= 200:
    print(f'O preço da passagem será: R$ {distancia*0.5}')
else:
    print(f'O preço da passagem será: R$ {distancia*0.45}')