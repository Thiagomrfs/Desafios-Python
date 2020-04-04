# tenha uma tupla de 0 até 20 e quando o usuário colocar um número mostre ele por extenso


def vernum(x, y):
    if x > y:
        while x > y:
            x = int(input("\033[31mCOMANDO INVÁLIDO, POR FAVOR INSIRA UM VALOR VÁLIDO: \033[m"))
    return x


ext = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze',
       'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    user = int(input("Digite o número que você quer: "))
    user = vernum(user, 20)
    name = ext[user]
    print(f"O seu número por extenso é: {name}")