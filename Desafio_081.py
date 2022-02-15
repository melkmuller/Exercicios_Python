# Exercício Python 081: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.

valores=[]
while True:
    valores.append(int(input("Digite um valor: ")))
    verificador = input("Deseja continuar? S/N: ").upper()
    if verificador != "S":
            break
print(f'Foram digitados {len(valores)} valores')
print('A lista de valores em ordem decrescente: ', sorted(valores))
print("O valor 5 está na lista" if 5 in valores else "O valor 5 não foi digitado")