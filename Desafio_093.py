# Exercício Python 093: Crie um programa que gerencie o aproveitamento de um jogador de futebol. 
# O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida.
# No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

jogador = dict()

jogador['nome'] = str(input("Nome do jogador: "))
jogador['partidas'] = int(input("Quantidade de partidas: "))
jogador['gols'] = list()

for v in range(jogador['partidas']):
    jogador['gols'].append(int(input(f" - Gols na partida {v+1}: ")))
jogador['total de gols'] = sum(jogador['gols'])

# Saída de dados
for chave, valor in jogador.items():
    print(f'    - {chave}: {valor}')