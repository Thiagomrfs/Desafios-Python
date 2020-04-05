#gere 5 números aleatórios e coloque numa tupla, depois mostre os valores e qual o maior e menor
from random import randint

num = (randint(1, 100), randint(1, 100), randint(1, 100), randint(1, 100), randint(1, 100))
maior = max(num)
menor = min(num)
print(num)
print(f"{maior} é o maior valor e {menor} é o menor valor.")