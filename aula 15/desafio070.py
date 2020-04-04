# leia o nome e o preço de vários produtos, pergunta se quer continuar, mostre o total  gasto na compra, quantos
# produtos custam mais de 1000 reais e o nome do produto mais barato


def ver(x, y):
    if x not in y:
        while x not in y:
            x = input("\033[31mCOMANDO INVÁLIDO, POR FAVOR INSIRA UM VALOR VÁLIDO: \033[m")
    return x


sum = 0
resp = ""
count = 0
plus1000 = 0
NameCheap = 0
minorPrice = 0
minorName = ""

while resp in "sS":
    count += 1
    print("-="*20)
    print(f"{count}º produto")
    name = input("Insira o nome do produto: ")
    price = float(input("Insira o preço do produto: "))
    sum += price
    if count == 1:
        minorPrice = price
        minorName = name
    else:
        if price < minorPrice:
            minorName = name
            minorPrice = price
    if price > 1000:
        plus1000 += 1
    resp = input("quer continuar[S/N]? ")
    if resp not in "sS":
        resp = ver(resp, "NnSs")

print(f"""
Você cadastrou {count} produtos;
Total gasto na compra: ${sum:.2f};
Existem {plus1000} produtos acima de $1000;
Custando ${minorPrice:.2f}, {minorName} é o produto mais barato.
""")