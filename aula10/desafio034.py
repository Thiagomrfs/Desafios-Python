# leia 3 retas e diga se elas podem formar um triângulo
r1 = int(input("Digite o cumprimento da primeira reta: "))
r2 = int(input("Digite o cumprimento da segunda reta: "))
r3 = int(input("Digite o cumprimento da terceira reta: "))

if +(r2 - r3) < r1 < (r2 + r3):
    print("\nA união dessas retas pode sim formar um triângulo.")
else:
    print("\nA união entre essas retas não pode formar um triângulo.")
print("Obrigado por utilizar o nosso sistema!!!".upper())