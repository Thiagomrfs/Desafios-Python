#simule o funcionamento de um caixa eletrônico, pergunte o usuário o valor a ser sacado, e o programa vai inforar
# quantas cédulas serão entregues, utilize cédulas de 50, 20, 10 e 1


def nota(x, y):
    if x >= 1:
        x = f"Você receberá {x} notas de ${y}."
        return x

def ver(x, y):
    if x not in y:
        while x not in y:
            x = input("\033[31mCOMANDO INVÁLIDO, POR FAVOR INSIRA UM VALOR VÁLIDO: \033[m")
    return x


resp = "s"
count50 = 0
count20 = 0
count10 = 0
count1 = 0

while resp in "sS":
    count50 = 0
    count20 = 0
    count10 = 0
    count1 = 0
    print("-="*20)
    print("Sistema de saque")
    valor = float(input("Qual o valor a ser sacado? $"))
    print("-=" * 20)
    while valor != 0:
        if valor >= 50:
            count50 += 1
            valor -= 50
        elif valor >= 20:
            count20 += 1
            valor -= 20
        elif valor >= 10:
            valor -= 10
            count10 += 1
        elif valor >= 1:
            valor -= 1
            count1 += 1

    print("-*"*20)
    if count50 > 0:
        print(f"{nota(count50, 50)}")
    if count20 > 0:
        print(f"{nota(count20, 20)}")
    if count10 > 0:
        print(f"{nota(count10, 10)}")
    if count1 > 0:
        print(f"{nota(count1, 1)}")
    print("-*"*20)

    resp = input("Deseja fazer outro saque[S/N]? ")
    if resp not in "sS":
        resp = ver(resp, "NnSs")
