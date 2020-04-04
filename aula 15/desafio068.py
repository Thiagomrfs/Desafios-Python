# faça um programa que jogue par ou impar com o computador, o jogo se´ra interrompido quando o jogador perder e
# mostra a quantidade de vitórias dele
from random import randint
from time import sleep


winner = "jogador"
count = 0

while winner == "jogador":
    print("\033[34mVAMOS JOGAR PAR OU ÍMPAR!!!!\033[m")
    chose = input("IMPAR OU PAR? ").upper().strip()
    user = int(input("Escolha um número de 1 a 10: "))
    pc = randint(1, 10)
    if chose == "PAR":
        if (user + pc) % 2 == 0:
            sleep(1)
            print("-="*20)
            print("O JOGADOR GANHOU!!!")
            winner = "jogador"
            count += 1
            print("-="*20)
        else:
            sleep(1)
            print("-="*20)
            winner = "computador"
            print("O COMPUTADOR GANHOU!!!")
            print("-="*20)
    if chose in "ÍMPARIMPAR":
        if (user+pc) % 2 != 0:
            sleep(1)
            print("-="*20)
            print("O JOGADOR GANHOU!!!")
            count += 1
            winner = "jogador"
            print("-="*20)
        else:
            sleep(1)
            print("-="*20)
            print("O COMPUTADOR GANHOU!!!")
            winner = "computador"
            print("-="*20)
print(f"você ganhou {count} vezes!")
print("ORBRIGADO POR JOGAR!!!")