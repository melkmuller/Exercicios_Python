#Calcular gratificações de Páscoa

#Entrada de dados
nome = input("Informe o nome do empregado: ")
hextras = float(input("Informe a quantidade de horas extras trabalhadas: "))
faltas = float(input("Informe a quantidade em horas de faltas do empregado: "))

#Processamento de dados
ht = hextras - 0.6666 * faltas

if ( ht >= 40):
    print(nome.title() + " tem direito a R$ 1.000,00 de gratificação")

elif (ht < 40 and ht >= 30):
    print(nome.title() + " tem direito a R$ 800,00 de gratificação")

elif (ht < 30 and ht >= 20):
    print(nome.title() + " tem direito a R$ 600,00 de gratificação")

elif (ht < 20 and ht >= 10):
    print(nome.title() + " tem direito a R$ 400,00 de gratificação")

else:
    print(nome.title() + " tem direito a R$ 200,00 de gratificação")