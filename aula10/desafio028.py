# pegue um número random e peça para o usuário adivinhar (entre 0 e 5)
import random

var = random.randint(1, 6)
resp = int(input("Irei pensar em um número de 1 a 5. Tente adivinhar: "))

if resp == var:
    print("Você acertou! Parabéns!!!!")
else:
    print("Errou!!! Tente novamente")
