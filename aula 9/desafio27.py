# leia o nome completo de alguém e mostre o primeiro e o último nome da pessoa
name = input("digite o seu nome completo: ")
div = name.split()

print(f"Seu primeiro nome é {div[0]} e o último é {div[len(div) - 1]}")