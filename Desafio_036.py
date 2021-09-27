#Desafio_036

#Entrada de dados
casa = float(input("Valor da casa: R$ "))
salario = float(input("Salário do comprador: R$ "))
anos = int(input("Por quantos anos deseja pagar? "))
minimo = salario * 0.30

#Processamento de dados
prestacao = casa / (anos * 12) 

#Saída de dddos
print("Para pagar uma casa de R${:.2f} em {} anos, a prestação será de R${:.2f}".format(casa, anos, prestacao))


#Condição para tomar o empréstimo
if prestacao <= minimo:
    print('Empréstimo PODE ser concedido')
else:
    print('Empréstimo NEGADO')