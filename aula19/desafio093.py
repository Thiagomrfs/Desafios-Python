# gerencie o aproveitamento de um jogador de fut: leia o nome de um jogador e a quantidade de partidas, 
# deois a quantidade de gols em cada partida. No final guarde tudo isso em um
# dicionário, incluindo a quantidade de gols feitos no campeonato.

jogador = {}

jogador["nome"] = input("Insira o nome do jogador: ")
jogador["quant"] = int(input("Insira a quantidade de partidas disputadas: "))
print()

aux = {}
gols = 0
for c in range(1, jogador["quant"]+1):
    aux[f"partida {c}"] = int(input(f"Insira a quantidade de gols realizados na partida {c}: "))
    gols += aux[f"partida {c}"]
jogador["partidas"] = aux
jogador["gols"] = gols

print()
print(f"""
Jogador: {jogador["nome"]}
Partidas: {jogador["quant"]} partidas
Gols no campeonato: {jogador["gols"]} gols
""")