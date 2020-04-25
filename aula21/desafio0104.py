# crie uma função leiaint, tipo o input, mas que só valida se for um valor numérico

def leiaInt():
    num = input("sla man colloca um numero ae: ")
    while num.isnumeric() != True:
        num = input("\033[31mInsira um valor numérico: \033[m")
    return num


aaa = leiaInt()
print(aaa)
