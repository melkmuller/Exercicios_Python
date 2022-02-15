# Exercício Python 079: Crie um programa onde o usuário possa digitar vários valores 
# numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. 
# No final, serão exibidos todos os valores únicos digitados, em ordem crescente. 

valores=[]
while True:
    numero = int(input("Digite um numero inteiro: "))
    if numero in valores:
        print(f'O número {numero} já existe na lista')
    else:
        valores.append(numero)
    verificador = input("Deseja continuar? [S/N]: ").upper()
    if verificador != "S":
            break
valores.sort()
print(valores)  