#lanchonete

#Escolher um item de alimentação
print("Esse é nosso cardápio: ")
print("1 - Hambúrguer R$4.50")
print("2 - Chessburguer R$5.50")
print("3 - Cachorro Quente R$ 4.00")
print("4 - Sanduíche R$ 3.50")
print("5 - Refrigerante R$ 1.00")
print("6 - Suco de Laranja R$ 2.00")
print("7 - Milk Shake R$ 1.50")
print("8 - Sundae R$ 3.00")
print("9 - Casquinha R$ 1.00")
print(" ")

#Processamento dos dados
print("Escolha um item de alimentação do nosso cardápio - 1, 2, 3 ou 4")
alimentacao = (int(input("Digite o número do item escolhido: ")))
  
if (alimentacao == 1):
    total1 = 4.50
elif (alimentacao == 2):
    total1 = 5.50
elif (alimentacao == 3):
    total1 = 4  
elif (alimentacao == 4):
    total1 = 3.50
else:
    print("Escolha um item de alimentação!")

print("Escolha uma bebida do nosso cardápio - 5 ou 6")
bebida = (int(input("Informe o número do item desejado: ")))

if (bebida == 5):
    total2 = 1
elif (bebida == 6):
    total2 = 2
else:
    print("Escolha uma bebida!")

print("Escolha uma sobremesa do nosso cardápio - 8 ou 9")
sobremesa = (int(input("Informe o número do item desejado: ")))

if(sobremesa == 7):
    total3 = 1.50
elif(sobremesa == 8):
    total3 = 3
elif(sobremesa == 9):
    total3 = 1
else:
    print("Escolha uma sobremesa!")

total = total1 + total2 + total3
print("O total do pedido foi de R$ ", total)




