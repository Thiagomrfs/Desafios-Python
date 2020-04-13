# leia vários valores e depois crie 2 listass extras: uma com os impares e uma com pares, dps mostre as 3
list = []
even = []
odd = []


def ver(x, y):
    if x not in y:
        while x not in y:
            x = input("\033[31mCOMANDO INVÁLIDO, POR FAVOR INSIRA UM VALOR VÁLIDO[S/N]: \033[m").upper()
    return x


while True:
    num = int(input("insira um número: "))
    list.append(num)
    if num % 2 == 0:
        even.append(num)
    elif num % 2 != 0:
        odd.append(num)
    resp = input("deseja continuar[S/N]? ").upper()
    resp = ver(resp, "SN")
    if resp == "N":
        break

print(f"""
todos os números: {list}
números pares: {even}
números ímpares: {odd}
""")