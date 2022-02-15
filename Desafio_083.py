# Exercício Python 083: Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. 
# Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.

expressao = str(input("Digite a expressão: "))
pilha = list[]
for caractere in expressao:
    if caractere == '(':
        pilha.append('(')
    elif caractere == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão é válida!')
else:
    print('Sua expressão é errada!')