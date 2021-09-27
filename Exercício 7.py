#Algoritmo que lê matrícula, notas e depois calcula o conceito

#Entrada de dados:
matricula = input("Informe a matrícula do aluno: ")
vp1a = float(input("Informe a nota obtida na Verificação Parcial 1A: "))
vp1b = float(input("Informe a nota obtida na Verificação Parcial 1B: "))
vp2 = float(input("Informe a nota obtida na Verificação Parcial 2: "))
me = float(input("Informe a média dos exercícios: "))

#Processamento dos dados
ma = (vp1a + vp1b * 2 + vp2 * 3 + me) / 7

#Saída de dados condicionada ao conceito
if (ma >= 9):
    print("Matrícula " + str(matricula))
    print(" VP1A: ", vp1a)
    print(" VP1B: ", vp1b)
    print(" VP2: ", vp2)
    print(" Média dos Exercícios: ", me)
    print("Teve média de aproveitamento de: " + str(ma) + ", conceito 'A', está Aprovado" )

elif (ma < 9 and ma >= 7.5):
    print("Matrícula " + str(matricula))
    print(" VP1A: ", vp1a)
    print(" VP1B: ", vp1b)
    print(" VP2: ", vp2)
    print(" Média dos Exercícios: ", me)
    print("Teve média de aproveitamento de: " + str(ma) + ", conceito 'B', está Aprovado" )

elif (ma < 7.5 and ma >= 6):
    print("Matrícula " + str(matricula))
    print(" VP1A: ", vp1a)
    print(" VP1B: ", vp1b)
    print(" VP2: ", vp2)
    print(" Média dos Exercícios: ", me)
    print("Teve média de aproveitamento de: " + str(ma) + ", conceito 'C', está Aprovado" )

elif (ma < 6 and ma >= 4):
    print("Matrícula " + str(matricula))
    print(" VP1A: ", vp1a)
    print(" VP1B: ", vp1b)
    print(" VP2: ", vp2)
    print(" Média dos Exercícios: ", me)
    print("Teve média de aproveitamento de: " + str(ma) + ", conceito 'D', está Reprovado" )

else:
    print("Matrícula " + str(matricula))
    print(" VP1A: ", vp1a)
    print(" VP1B: ", vp1b)
    print(" VP2: ", vp2)
    print(" Média dos Exercícios: ", me)
    print("Teve média de aproveitamento de: " + str(ma) + ", conceito 'E', está Reprovado" )