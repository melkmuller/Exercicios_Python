#Exercício 3
#calcular número de tijolos necessários para construir uma parede
#calcular o custo de construção, referente aos tijolos

#Entrada de dados
print("Primeiro informe os valores da altura e comprimento do tijolo em Centímetros.")
a_tijolo = float(input("Altura do tijolo: "))
c_tijolo = float(input("Comprimento do tijolo: "))

print("Agora informe as medidas da parede em Metros: ")
a_parede = float(input("Altura da parede: "))
c_parede = float(input("Comprimento da parede: "))
milheiro = float(input("Insira o valor do milheiro em Reais: "))

#Processamento dos dados

#Calcular área do tijolo, e transformar em metros
area_tijolo = (a_tijolo * c_tijolo) / 100

#Calcular a área efetiva da parede, contando que a argamassa ocupa 10% da área
area_parede = (a_parede * c_parede) * 0.9

#Calcular número de tijolos
n_tijolos = (area_parede / area_tijolo)

#Calcular custo dos tijolos 
custo = (milheiro / 1000) * n_tijolos

#Saída de dados
print("Você precisará de :" + str(n_tijolos) + " tijolos")
print("Isso irá custar: R$ " + str(custo))

