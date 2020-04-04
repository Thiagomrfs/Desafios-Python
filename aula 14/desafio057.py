# Faça um programa que leia o sexo de uma pessoa que só aceite M ou F, caso esteja errado, peça
# a dgitação novamente até ficar certo

sexo = input("Digite o seu sexo[M/F]: ").strip().upper()[0]
while sexo not in "FfMm":
    sexo = input("Dados inválidos, por favor digite o seu sexo[M/F]: ")
print("Sexo cadastrado com sucesso")