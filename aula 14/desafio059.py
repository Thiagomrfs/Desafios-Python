from time import sleep


def menu():
    det = "-="
    resp = 0
    print(f"\033[36m{det*20}")
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))
    print(f"{det*20}\033[m")
    while resp != 5:
        sleep(1)
        esc = int(input("""
okok, o que você que fazer?
[1] - SOMAR
[2] - MULTIPLICAR
[3] - MAIOR
[4] - ESCOLHER NOVOS NÚMEROS
[5] - SAIR DO PROGRAMA
Digite a sua resposta: """))

        if esc == 1:
            sleep(1)
            print(f"\n\033[34m{det*20}")
            print(f"A soma entre os dois números é: {num1+ num2}")
            print(f"{det * 20}\033[m")
        elif esc == 2:
            sleep(1)
            print(f"\n\033[34m{det * 20}")
            print(f"O produto entre {num1} e {num2} é: {num1*num2}")
            print(f"{det * 20}\033[m")
        elif esc == 3:
            sleep(1)
            maior = 0
            if num1 > num2:
                maior = num1
            else:
                maior = num2
            print(f"\n\033[34m{det * 20}")
            print(f"O maior número entre {num1} e {num2} é: {maior}")
            print(f"{det * 20}\033[m")
        elif esc == 4:
            sleep(1)
            menu()
        elif esc == 5:
            sleep(1)
            resp = 5
        else:
            sleep(1)
            print(f"\n\033[31m{det * 20}")
            print("Caractere inválido".upper())
            print(f"{det * 20}\033[m\n")
            menu()
    sleep(1)
    print(f"\n\032[34m{det * 20}")
    print("Obrigado por utilizar o nosso programa")
    print(f"{det * 20}")
    exit(0)


menu()
