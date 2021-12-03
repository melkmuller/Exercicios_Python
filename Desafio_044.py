print('{:=^40}'.format(' LOJAS MÜLLER '))
print('_'*40)
compra = float(input(('Informe o valor dotal da compra: R$ ')))
print('_'*40)
print('{:=^40}'.format(' FORMA DE PAGAMENTO '))

# Menu de formas de pagamento
print('''[1] à vista dinheiro/cheque
[2] à vista cartão
[3] 2x no cartão
[4] 3x ou mais no cartão
========================''')

# Recebimento da forma de pagamento
opcao = int(input('Qual a opção desejada? '))

#Processamento dos dados
if opcao == 1:
    print(f'Sua compra de R$ {compra} terá 10% de desconto, totalizando R$ {compra * 0.9}')

elif opcao == 2:
    print(f'Sua compra de R$ {compra} terá 5% de desconto, totalizando R$ {compra * 0.95}')

elif opcao == 3:
    print(f'O total de sua compra permanece em R$ {compra}, em 2x de R$ {compra/2}')

elif opcao == 4:
    parcelas = int(input('Informe a quantidade de parcelas: '))
    total = compra * 1.2
    print(f'Sua compra será parcelada em {parcelas}x de {total/parcelas}, com Juros')
    print(f'Sua compra de R$ {compra} custará  R$ {total} no total')
else:
    print('Opção inválida!')

