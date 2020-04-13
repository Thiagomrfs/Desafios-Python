# leia vários números e diga a quantidade de valores, lista decrescente e se o 5 estpa na lista
list = []
count = 0


def ver(x, y):
    if x not in y:
        while x not in y:
            x = input("\033[31mCOMANDO INVÁLIDO, POR FAVOR INSIRA UM VALOR VÁLIDO[S/N]: \033[m").upper()
    return x


while True:
    num = int(input(f"insira o {count+1}º número: "))
    list.append(num)
    sorted(list)
    count += 1
    resp = input("deseja continuar[S/N]? ").upper()
    resp = ver(resp, "SN")
    if resp == "N":
        break

has5 = ""
if 5 in list:
    has5 = "tem"
else:
    has5 = "não tem"

print(f"""
você digitou {count} valores.
a sua lista decrescente ficou: {sorted(list, reverse=True)}
na sua lista {has5} o número 5
""")