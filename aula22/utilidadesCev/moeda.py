def adicionar(num, adc, formatar=False):
    num = num * (100+adc)/100
    if formatar == True:
        return formatado(num)
    else:
        return num

def diminuir(num, dim, formatar=False):
    num = num * (100-dim)/100
    if formatar == True:
        return formatado(num)
    else:
        return num

def dobro(num, formatar=False):
    num = num * 2
    if formatar == True:
        return formatado(num)
    else:
        return num

def metade(num, formatar=False):
    num = num/2
    if formatar == True:
        return formatado(num)
    else:
        return num

def formatado(num):
    return f"R$ {num:.2f}"

def resumo(num):
    print(f"""
    ==================================
                 Resumão
    ==================================
    {"dobro".ljust(25, ".")} {dobro(num, True)}
    {"Adicionar".ljust(25, ".")} {adicionar(num, 10, True)}
    {"Retirar".ljust(25, ".")} {diminuir(num, 10, True)}
    {"metade".ljust(25, ".")} {metade(num, True)}
    """)