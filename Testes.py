n = input("Digite algo: ")
print(type(n))
print(n.isnumeric())
print(n.isalpha())
print(n.isalnum())

# Ordem de precedência dos operadores aritméticos
# 1-Parênteses ()
# 2-Potências **
# 3-Multiplicação *, Divisão /, Divisão inteira //, Resto da Divisão % (na ordem de aparecimento da esquerda-direita)
# 4-Mais e Menos (na ordem de aparecimento da esquerda-direita)

#Para limitar casas decimais num format - {:.Xf} sendo o X o número de casas decimais que eu quero {:.2f} mostrará duas casas flutuantes

#Para não quebrar a linha e juntar dois prints, colocar end=''