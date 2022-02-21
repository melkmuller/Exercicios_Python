# Exercício Python 015: Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. 
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

#Entrada de dados
km_percorrido = int(input("Quantos kilômetros foram rodados: "))
dias_alugado = int(input("Quantos dias foi alugado?: "))

#Processamento com saída, sem uso de variável
print(f'O total do serviço de aluguel é de: R$ {(600*dias_alugado)+(km_percorrido*0.15):.2f}')