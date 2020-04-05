# leia 4 valores e diga quantas vezes apareceu o 9, quando apareceu o primeiro 3 e quais são os pares

n1 = int(input("Insira um número: "))
n2 = int(input("outro: "))
n3 = int(input("outro: "))
n4 = int(input("outro: "))

tup = (n1,n2,n3,n4)
is9 = 0
pares = list()

for c in tup:
    if c == 9:
        is9 += 1
    if c % 2 == 0:
        pares.append(c)

print(f"""
Nos números apresentados apareceram {is9} noves.
o primeiro 3 aparece na posição {tup.index(3) + 1}
os números {pares} são pares.
""")
