# leia uma expressão qualquer que use parênteses, o programa deve dizer se os parenteses estão arbetos e fechados na
# ordem certa


def ver(x, y):
    if x not in y:
        while x not in y:
            x = input("\033[31mCOMANDO INVÁLIDO, POR FAVOR INSIRA UM VALOR VÁLIDO[S/N]: \033[m").upper()
    return x


quant = []

while True:
    exp = input("Insira a sua expressão: ")
    for letter in exp:
        if letter == "(":
            quant.append("(")
        else:
            if len(quant) != 0:
                quant.pop()
                print("tirei um parentese")
            elif len(quant) == 0:
                quant.append(")")
                break
                print("TAVA ZERADO, ADICIONEI UM )")
    print(len(quant))
    if len(quant) == 0:
        print("\033[34mSua expressão é válida!\033[m")
    else:
        print("\033[31mSua expressão NÃO é válida!\033[m")
    resp = input("deseja continuar[S/N]? ").upper()
    resp = ver(resp, "SN")
    if resp == "N":
        break
    elif resp == "S":
        quant = []
