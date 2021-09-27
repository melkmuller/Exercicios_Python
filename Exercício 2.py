#Exercício 2
#Equações lineares

#Entrada de dados
a = float(input("Informe o valor de a: "))
b = float(input("Informe o valor de b: "))
c = float(input("Informe o valor de c: "))
d = float(input("Informe o valor de d: "))
e = float(input("Informe o valor de e: "))
f = float(input("Informe o valor de f: "))

#Processamento dos dados
x = (c * e ) - (b * f) / (a * e) - (b * d)
y = (a * f ) - (c * d) / (a * e) - (b * d)

#Saída dos dados
print("Com os valores informados acima, temos o seguinte resultado:  ")
print("X = ", x)
print("y = ", y)