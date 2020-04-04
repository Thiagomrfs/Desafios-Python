#  JOKEMPÔ
import random
from time import sleep
itens = ("Pedra", "Papel", "Tesoura")
pc = random.randint(0,2)

print("""Escolha a sua opção: 
0 ) Pedra
1 ) Papel
2 ) Tesoura
""")
user = int(input("Eu escolho: "))

print("JO")
sleep(1)
print("KEN")
sleep(1)
print("PÔ")
sleep(1)

print("-="*12)
print(f"\033[36mComputador jogou {itens[pc]}")
print(f"\033[36mJogador jogou {itens[user]} \033[m")
print("-="*12)

if pc == 0: # PEDRA
    if user == 0:
        print("\033[30m EMPATE")
    elif user == 1:
        print("\033[32m JOGADOR VENCE")
    elif user == 2:
        print("\033[31m COMPUTADOR VENCE")
    else:
        print("\033[31m COMANDO INVÁLIDO")
elif pc == 1: # PAPEL
    if user == 1:
        print("\033[30m EMPATE")
    elif user == 2:
        print("\033[32m JOGADOR VENCE")
    elif user == 0:
        print("\033[31m COMPUTADOR VENCE")
    else:
        print("\033[31m COMANDO INVÁLIDO")
elif pc == 2: # TESOURA
    if user == 2:
        print("\033[30m EMPATE")
    elif user == 0:
        print("\033[32m JOGADOR VENCE")
    elif user == 1:
        print("\033[31m COMPUTADOR VENCE")
    else:
        print("\033[31m COMANDO INVÁLIDO")
else:
    print("\033[31m COMANDO INVÁLIDO")