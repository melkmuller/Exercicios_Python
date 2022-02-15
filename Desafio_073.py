    #  Exercício Python 073: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
    # a) Os 5 primeiros times.
    # b) Os últimos 4 colocados.
    # c) Times em ordem alfabética. 
    # d) Em que posição está o time da Chapecoense.

times = ("Atlétigo-MG","Flamengo","Palmeiras","Fortaleza","Corinthians","Bragantino","Fluminense","América-MG","Atlético-GO","Santos",
            "Ceará", "Internacional","São Paulo","Athletico-PR","Cuiabá","Juventude",
            "Grêmio","Bahia","Sport Recife","Chapecoense")

print(f'Lista de times: {times}')
# for t in times:
#     print(t)

print(f'Os cinco primeiros colocados são: {times[0:5]}')
print(f'Os times da zona de rebaixamento são: {times[-4:]}')
print(f'Times em ordem alfabática: {sorted(times)}')
print(f'A Chapecoense está na {times.index("Chapecoense")+1}ª posição')