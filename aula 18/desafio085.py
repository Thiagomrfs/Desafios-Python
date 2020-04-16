# leia 7 valores e cadastre em *uma lista* que mantenha separados os pares e impares
listaPrincipal = []
pares = []
impares = []

for c in range(0,8):
    num = int(input("Insira o número: "))
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)

listaPrincipal.append(pares)
listaPrincipal.append(impares)

print(f"\nNúmeros pares: {listaPrincipal[0]}")
print(f"Números impares: {listaPrincipal[1]}")