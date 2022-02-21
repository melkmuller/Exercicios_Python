# Exercício Python 095: Aprimore o desafio 93 para que ele funcione com vários jogadores, 
# incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.

todos = list()
while True:
    jogador = dict()
    nome = input('Nome do jogador: ').strip()
    npart = int(input(f'Quantas partidas {nome} jogou? '))
    gols = list()
    tot = 0
    for c in range(1, npart+1):
        p = int(input(f'   -Gols na {c}ª partida: '))
        gols.append(p)
        tot += p
    jogador = {
        'nome': nome,
        'gols': gols,
        'total': tot }
    todos.append(jogador.copy())
    opc = input('Quer continuar? [S/N] ').strip().lower()
    if opc != 's' and opc != 'n':
        print('ERRO: Digite apenas S ou N (SIM ou NÃO)')
        while opc != 's' and opc != 'n':
            opc = input('Quer continuar? [S/N] ').strip().lower()
    if opc == 'n':
        break
print(f'{"-=-"*20}\ncod nome{" "*11}gols{" "*11}total\n{"-"*40}')
for j in todos:
    sla = f'{todos.index(j):>3} {j["nome"]}{" "*(20-len(j["nome"])-5)}{j["gols"]}'
    print(f'{sla}{" "*(34-len(sla))}{j["total"]}')
while True:
    print('-'*40)
    opt = int(input('Mostrar dados de qual jogador? [Digite 999 para sair] '))
    if opt < 0 or opt > len(todos)-1:
        while opt < 0 or opt > len(todos)-1:
            if opt == 999:
                break
            print(f'ERRO: Não existe jogador com o código {opt}.')
            opt = int(input('Mostrar dados de qual jogador? [Digite 999 para sair] '))
    if opt == 999:
        break
    for i in todos:
        if opt == todos.index(i):
            print(f'  -- Levantamento do Jogador {i["nome"]}')
            for jog in range(0, len(i['gols'])):
                print(f'    >> No jogo {jog+1} fez {i["gols"][jog]} gols')
print(f'{"-"*40}\n<<< VOLTE SEMPRE >>>')