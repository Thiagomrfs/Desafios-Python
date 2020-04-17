# crie palpites na mega sena, pergunte quaantos palpites vão ser e gere 6 números entre 1 e 60 pra cada,
# colocando tudo em uma lista composta. (sem repetir no mesmo jogo)
import random

jogos = []
quant = int(input("Quantos jogos vão ser? "))

for j in range(0, quant):
    chutes = []
    for val in range(0, 6):
        num = random.randint(1, 61)
        chutes.append(num)
    jogos.append(chutes)

print("\n", "-=" * 24)

for j in range(0, quant):
    print(f"seu {j+1}º jogo é: {jogos[j]}")

print("-="*9, "<Boa Sorte>", "-="*9)