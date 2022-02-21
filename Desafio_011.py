# Exercício Python 011: Faça um programa que leia a largura e a altura de uma parede em metros, 
# calcule a sua área e a quantidade de tinta necessária para pintá-la, 
# sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

#Entrada de dados
largura = float(input('Digite a largura da parede (m): '))
altura = float(input("Digite a altura da parede (m): "))

#Processamento dos dados
area = largura * altura
tinta = area /2 

#Saída de dados
print(f'Sua parede tem {area}m²')
print(f'Será necessário um total de {tinta:.2f} litros de tinta')