# função ficha que receba dois param, p nome de um jogador e a quantidade de gols, o programa deve mostrar a
# ficha mesmo que algum param não esteja correto

def ficha(jogador="Desconhecido", gols=0):
    print(f"O jogador {jogador} fez {gols} gols no campeonato")


ficha('julio', 1)
ficha(gols=98)
ficha('trevor', )
ficha('iniesta', 1992)
ficha()