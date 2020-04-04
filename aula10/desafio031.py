# leia um ano e diga se ele é bissexto
import math
ano = int(input("Digite um ano: "))
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print("Esse ano é bissexto!")
else:
    print("Esse ano não é bissexto!")
print("Obrigado por utilizar o nosso sistema!".upper())