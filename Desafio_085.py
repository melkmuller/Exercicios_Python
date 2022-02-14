# Exercício Python 085: Crie um programa onde o usuário possa digitar sete 
# valores numéricos e cadastre-os em uma lista única que mantenha separados 
# os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.

#Primeira forma 
# valores = list()
# pares = list()
# impares = list()
# for n in range(7):
#     num = int(input("Digite um valor: "))
#     if num % 2 == 0:
#         pares.append(num)
#     else:
#         impares.append(num)
# pares.sort()
# impares.sort()
# valores.append(pares[:])
# valores.append(impares[:])
# print(valores)


#Forma otimizada
valores = [[],[]]
for v in range(7):
    numero = int(input('Digite um valor: '))
    if numero % 2 == 0:
        valores[0].append(numero)
    else:
        valores[1].append(numero)

print(f'Os números pares foram: {sorted(valores[0])}')
print(f'Os números ímpares foram: {sorted(valores[1])}')
