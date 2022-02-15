# Exercício Python 076: Crie um programa que tenha uma tupla única com nomes de
# produtos e seus respectivos preços, na sequência. No final, mostre uma listagem de preços, 
# organizando os dados em forma tabular.

listaDeProdutos = ('Lápis',1.75,
                    'Borracha', 0.50,
                    'Caderno', 15.60,
                    'Compasso', 8.40,
                    'Apontador', 0.80,
                    'Caneta Azul', 2.25,
                    'Tesoura', 3.60)

print("{:=^30}".format(" LISTA DE PRODUTOS "))
for pos in range(0,len(listaDeProdutos),2):
    print(f'{listaDeProdutos[pos]:.<20}', f'R$ {listaDeProdutos[pos+1]:6.2f}')