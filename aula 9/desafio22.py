# leia um nome completo e mostre: com letras maúsculas, minúsculas, quantas letras
# ao todo -espaços e quantidade de letras no primeiro nome
#upper, lower, len

var = input("Digite o seu nome completo: ")

print(f"""Seu nome quando colocado em letras maiúsculas é: {var.upper()}
Seu nome quando colocado em letras minúsculas é: {var.lower()}
A quantidade de letras presentes no seu nome é: {len(var) - var.count(" ")}
A quantidade de letras presentes no seu primeiro nome é: {len(var.split()[0])}""")

# mission complete