#reescreva a func leiainte da aula 104 incluindo a possibilidade de colocarem um tipo errado e faça outra p/ float

def leiaInt():
    num = input("Insira um valor inteiro: ")
    try:
        return int(num)
    except:
        while True:
            num = input("\033[31mInsira um valor Inteiro: \033[m")
            if num.isnumeric() == True:
                num = int(num)
                break
        return num


def leiaFloat():
    num = input("Insira um valor numérico: ")
    try:
        return float(num)
    except:
        while type(num) != float:
            num = input("\033[31mInsira um valor numérico: \033[m")
            try:
                return float(num)
            except:
                pass


if  __name__ == "__main__":
    a = leiaInt()
    print(a)
    b = leiaFloat()
    print(b)