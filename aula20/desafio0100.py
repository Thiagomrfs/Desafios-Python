# crie uma lista chamada numeros e duas funções chamadas sorteio e somaPar a sorteio vai sortear 5 numeros
# colocar na lista e a somaPar vai somar todos os pares sorteados
from random import randint

numeros = []


def sorteio(database):
    for c in range(0,5):
        database.append(randint(1, 60))


sorteio(numeros)


def somaPar(database):
    soma = 0
    for num in database:
        if num % 2 == 0:
            soma += num
    return soma


print(f"""
a lista: {numeros}
a soma: {somaPar(numeros)}
""")