# faça uma cópia da função max()
def ver(x, y):
    if x not in y:
        while x not in y:
            x = input("\033[31mCOMANDO INVÁLIDO, POR FAVOR INSIRA UM VALOR VÁLIDO: \033[m").capitalize()
    return x


db = []

while True:
    num = int(input("Insira um número: "))
    db.append(num)
    resp = input("deseja continuar? [S/N] ").capitalize()
    resp = ver(resp, 'SN')
    if resp == "N":
        break

def maior(database):
    maior = 0
    for num in database:
        if database.index(num) == 0:
            maior = num
        else:
            if num > maior:
                maior = num
    print(f"O maior número é: {maior}")

maior(db)