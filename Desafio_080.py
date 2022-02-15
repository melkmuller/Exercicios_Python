# Exercício Python 080: Crie um programa onde o usuário possa digitar cinco valores 
# numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()). 
# No final, mostre a lista ordenada na tela.

valores=[]
for c in range(5):
    num = int(input("Digite um número: "))
    if c==0 or num > valores[-1]:
        valores.append(num)
        print("O valor foi adicionado ao final da lista!")
    else:
        for c in range(5):
            if num <= valores[c]:
                valores.insert(c,num)
                print(f'O número foi adicionado na posição {c}')
                break
print(valores)
