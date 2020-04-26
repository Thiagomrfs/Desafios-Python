def msg(text, cor=""):
    print(f"\033[{cor}m"+"="*len(text))
    print(text)
    print("="*len(text)+"\033[m")


def verificarInt(analisado, espaço):
    try:
        analisado = int(input("Insira um valor: "))
        if analisado in espaço:
            return analisado
        else:
            print(propositalmente_errado)
    except:
        while True:
            try:
                analisado = int(input("\033[31mInsira um valor válido: \033[m"))
                if analisado in espaço:
                    return analisado
                    break
            except:
                pass
        return analisado


def verificarSN(analisado):
    try:
        analisado = input("Deseja continuar? [S/N] ").capitalize()
        if analisado in "SN":
            return analisado
        elif len(analisado) < 1:
            print(propositalmente_errado)
        else:
            print(propositalmente_errado)
    except:
        while True:
            try:
                analisado = input("\033[31mCOMANDO INVÁLIDO, POR FAVOR INSIRA UM VALOR VÁLIDO: [S/N] \033[m").capitalize()
                if analisado in "SN":
                    break
            except:
                pass
        return analisado