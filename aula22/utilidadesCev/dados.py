def verifica_num(num):
    while num.isnumeric() != True:
        num = input("\033[31mInsira um valor numérico: \033[m")
    return num

def leia_dinheiro():
    num = input("Insira um valor: ")
    if num.isnumeric() == False:
        if "," in num:
            num = num.replace(",", ".")
            return float(num)
        elif "." in num:
            return float(num)
        else:
            while num.isnumeric() != True:
                num = input("\033[31mInsira um valor numérico: \033[m")
            return float(num)
    return float(num)
