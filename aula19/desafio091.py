#4 jogadores joguem um dado(1 e 6) e tenha resultados aleatórios. guarde os resultados no dicionário e no fim coloque o dicionário
#  em ordem, sabendo que o vencedor é o maior valor
from random import randint
from time import sleep
from operator import itemgetter

count = 1

jogadores = {
    "jogador 1": randint(1,6),
    "jogador 2": randint(1,6),
    "jogador 3": randint(1,6),
    "jogador 4": randint(1,6)
}
ranking = {}

print("\nValores sorteados:")
for k,v in jogadores.items():
    print(f"{k:.<20} {v}")
    sleep(0.5)

ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
print("\nRanking:")
for c in ranking:
    print(f"{count}º - {c[0]}")
    count += 1