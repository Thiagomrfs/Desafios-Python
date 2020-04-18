# leia o nome e a média de um aluno e coloque em dicionário juntamente com a situação
def ver(x, y):
    if x not in y:
        while x not in y:
            x = input("\033[31mCOMANDO INVÁLIDO, POR FAVOR INSIRA UM VALOR VÁLIDO: \033[m").capitalize()
    return x


alunosdb = []
count = 1

while True:
    aux = {}
    print("-="*11, f"< {count}º aluno >", "-="*11)
    aux["aluno"] = input("Insira o nome do aluno: ").capitalize()
    aux["nota"] = float(input("Insira a nota do aluno: "))
    if aux["nota"] >= 6:
        aux["situação"] = "Aprovado"
    else:
        aux["situação"] = "Reprovado"
    alunosdb.append(aux)
    resp = input("deseja continuar[S/N]? ").upper()
    resp = ver(resp, "SNsn")
    count += 1
    if resp in "Nn":
        break

for a in alunosdb:
    print(f"{a['aluno']:.<20} {a['situação']}")