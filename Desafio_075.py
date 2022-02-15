# Exercício Python 075: Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:

# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.

numero = tuple(int(input("Digite um número: ")) for i in range(4))
print(f'O número nove aparece {numero.count(9)} vezes' if 9 in numero else "Nenhum número nove digitado")
print(f'O número três foi digitado pela primeira vez na posição {numero.index(3)+1}' if 3 in numero else "Não foi digitado o número três")
print("Os valores pares digitados foram: ", end='')
print({n for n in numero if n %2 == 0}, end='')

