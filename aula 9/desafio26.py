# leia uma frase e diga quantas vezes aparece a letra "a" e sua primeira e última aparição
# count, split
var = input("Digite uma frase: ")
frase = var.lower()
num = frase.count("a")

print(f'''\033[36m
    A quantidade total de letras na frase é: {len(var) - 1}
    A quantidade de "a" presente na frase é: {num}
    O primeiro "a" fica na posição: {frase.find("a")}
    E o último na: {frase.rfind("a")}
''')