# leia 5 números em for e diga qual o maior e qual o menor e as posições deles
list = []
for c in range(1, 6):
    num = int(input(f"Digite o {c}º número: ").strip())
    list.append(num)

print(f"""
Na posição {list.index(max(list))+1}, {max(list)} é o maior valor.
Na posição {list.index(min(list))+1}, {min(list)} é o menor valor.
""")
