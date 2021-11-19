n = int(input('Digite um número inteiro: '))
a = n - 1
s = n + 1
print("Analisando o valor {}, o seu antecessor é {}, e o seu sucessor é {}.".format(n, a, s))

# OU DE MANEIRA OTIMIZADA, SEM NECESSIDADE DE FUTURAS CONSULTAS DE VARIÁVEIS:

# n = int(input('Digite um número inteiro: '))
# print("Analisando o valor {}, o seu antecessor é {}, e o seu sucessor é {}.".format(n, (n-1), (n+1)))