#Calcular velocidade média, e quantidade de combustível gasto

#Entrada de dados
dist = int(input("Informe a distância percorrida em Kilômetros: "))
tempo = float(input("Informe o tempo total da viagem em horas: "))

#Processamento de dados, considerando o consumo de 12Km/l
velocidade_media = dist / tempo
combustível = dist / 12

#Saída de dados
print("Sua velocidade média na viagem foi de: " + str(velocidade_media) + "Km/h")
print("Seu carro consumiu: " + str(combustível) + " litros")