#Exercício 4
#Salários e abonos

#Entrada de dados
salario_bruto = float(input("Informe seu salário bruto: "))
salario_minimo = float(input("Informe o salário mínimo vigente: "))

#Processamento dos dados
ir = salario_bruto * 0.15
inss = salario_bruto * 0.05
abono = salario_minimo * 0.60
salario_liquido = (salario_bruto - ir - inss) + abono

#Saída de dados
print("Seu salário com desconto de INSS e Imposto de Renda, somando ao abono, resulta em R$ ", salario_liquido)

