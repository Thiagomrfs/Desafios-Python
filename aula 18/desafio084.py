# leia o nome e peso de várias pessoas e mostre: quantas pessoas foram cadastadas, uma lista com as pessoas mais
# pesadas e uma lista com as mais leves.

def ver(x, y):
    if x not in y:
        while x not in y:
            x = input("\033[31mCOMANDO INVÁLIDO, POR FAVOR INSIRA UM VALOR VÁLIDO[S/N]: \033[m").upper()
    return x

count = 1
pessoas = []
maisLeve = 0
maisPesado = 0
listpesadas = []
listleves = []

while True:
    cadastro = []
    print("-="*20)
    print(f"{count}º pessoa")
    nome = input("Insira o nome: ")
    peso = float(input("Insira o peso: "))
    print("-="*20)
    if count == 1:
        maisLeve = maisPesado = peso
    else:
        if peso < maisLeve:
            maisLeve = peso
        elif peso > maisPesado:
            maisPesado = peso
    cadastro.append(nome)
    cadastro.append(peso)
    pessoas.append(cadastro)
    resp = input("deseja continuar[S/N]? ").upper()
    resp = ver(resp, "SN")
    if resp == "N":
        break
    count += 1

for p in pessoas:
    if p[1] == maisLeve:
        listleves.append(p[0]) 
    elif p[1] == maisPesado:
        listpesadas.append(p[0])

print(f"\nForam cadastradas {count} pessoas.")
print(f"{listleves} são os mais leves")
print(f"{listpesadas} são os mais pesados")