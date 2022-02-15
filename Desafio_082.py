# Exercício Python 082: Crie um programa que vai ler vários números e colocar em uma lista. 
# Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores
# ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.

#Primeira forma, exatamente como pediu o enunciado:
valores=[]
pares=[]
impares=[]
while True:
    num = (int(input("Digite um valor: ")))
    valores.append(num)
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)
    verificador = input("Deseja continuar? S/N: ").upper()
    if verificador != "S":
            break
print(f'Todos os valores digitados foram: {valores}')
print(f'Todos os pares digitados foram: {pares}')
print(f'Todos os ímpares dgitados foram: {impares}')