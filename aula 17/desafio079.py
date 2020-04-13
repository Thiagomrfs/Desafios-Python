# leia vários valores numéricos e coloque em lista, se já tiver o número lá dentro ele não adiciona(só adc novos
# valores), depois mostre os valores em ordem crescente
list = []


def ver(x, y):
    if x not in y:
        while x not in y:
            x = input("\033[31mCOMANDO INVÁLIDO, POR FAVOR INSIRA UM VALOR VÁLIDO[S/N]: \033[m").upper()
    return x


while True:
    num = int(input("Digite o seu número: "))
    if num in list:
        print("O número já consta na lista.")
    else:
        print("Número adicionado com sucesso.")
        list.append(num)
    resp = input("Deseja continuar[S/N]? ").upper()
    resp = ver(resp, "SN")
    if resp == "N":
        break

print(f"""Seus números são:
{str(sorted(list)).strip("[]")}
""")
