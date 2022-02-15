# Exercício Python 072: Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
# Seu programa deverá ler um número pelo teclado (entre 0 e 10) e mostrá-lo por extenso.

#Declaração da tupla, para posterior consulta
extenso = ("zero","um","dois","três","quatro","cinco","seis","sete","oito","nove","dez")

#Variável a ser declarada pelo usuário
num = int(input("Digite um número de 0 a 10: "))

# Verifica se o número está entre 0 e 10
while num  not in range(0,11):
    num = int(input("Número inválido. Digite um número entre 0 e 10: "))
print(f'Você digitou o número {extenso[num]}')


