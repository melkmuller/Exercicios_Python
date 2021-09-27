#Programa que converte sistema de bases numéricas

#Entrada de dados
numero = int(input('Digite um número inteiro que deseja converter: '))

#Opções para escolha
print('''Escolha uma das bases para conversão:
[1] converter para BINÁRIO
[2] converter para OCTAL
[3] converter para HEXADECIMAL''')

#Receber a escolha do usuário
opcao = int(input('Escolha a opção desejada: '))

#Verificação e processamento dos dados
if opcao == 1:
    print('{} convertido para BINÁRIO equivale a: {}'.format(numero, bin(numero)[2:]))

elif opcao == 2:
    print('{} convertido para OCTAL equivale a: {}'.format(numero, oct(numero)[2:]))

elif opcao == 3:
    print('{} convertido para HEXADECIMAL equivale a: {}'.format(numero, hex(numero)[2:]))

else:
    print('opção inválida!')