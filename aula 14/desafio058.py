# refaça o desafio 28(jogo de adivinhar). Só que agora o jogador vai tentar até acertar
# no fim mostre a quantidade de palpites
import random
pc = random.randint(1, 5)
resp = ""
user = int(input("Vou pensar em um número, tente adivinhar[1 a 5]: "))
count = 1

while user != pc:
    user = int(input("Tente novamente: "))
    count += 1
print(f"OkOk, você acertou depois de {count} tentativas")
