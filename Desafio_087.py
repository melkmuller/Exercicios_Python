# Exercício Python 087: Aprimore o desafio anterior, mostrando no final: 
# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.

matriz = [[int(input(f'Dgite o número da posição [{j}]-[{i}]: ')) for i in range(3)] for j in range(3)]
somaPar = somaColuna= maiorValor = 0

print()
for l in range(3):
    for c in range(3):
        print(f'[{matriz[l][c]:^5}]',end="")
        if matriz[l][c] % 2 == 0:
            somaPar += matriz[l][c]
    print()

for l in range(3):
    somaColuna += matriz[l][2]

print()
print(f'A soma dos valores pares é: {somaPar}')
print(f'A soma dos valores da terceira coluna é: {somaColuna}')
print(f'O maior valor da segunda linha é: {max(matriz[1])}')