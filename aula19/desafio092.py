# leia nome, ano de nasc e carteira de trabalho de uma pessoa e cadastre-os com un dic(com idade) 
# e se a CTPS for diferente de 0 o dicionário recebrá tbm o ano de contratação e o salário
# calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar(35 anos de colaboração).
from datetime import datetime


def ver(x, y):
    if x not in y:
        while x not in y:
            x = input("\033[31mCOMANDO INVÁLIDO, POR FAVOR INSIRA UM VALOR VÁLIDO: \033[m").capitalize()
    return x


db = []
now = datetime.now()

while True:
    cadastro = {}
    cadastro["nome"] = input("Insira o nome da pessoa: ").capitalize()
    cadastro["idade"] = now.year - int(input("Insira o ano de nascimento: "))
    cadastro['CTPS'] = int(input("Insira o número da sua CTPS (0 se não tiver): "))
    if cadastro["CTPS"] != 0:
        cadastro["Contratação"] = int(input("Insira o ano de contratação: "))
        cadastro["Salário"] = int(input("Insira o salário: "))
        cadastro["Aposentadoria"] = (35 - (now.year - cadastro["Contratação"])) + cadastro["idade"]
    db.append(cadastro)
    
    resp = input("deseja continuar[S/N]? ").upper()
    resp = ver(resp, "SNsn")
    if resp in "Nn":
        break

nomes = []
for func in db:
    nomes.append(func["nome"])

print("\n\033[32mSeus dados foram guardados com sucesso.\033[m")
resp = input("Deseja consultar algum dado? [S/N] ").upper()
resp = ver(resp, "SN")

if resp == "S":
    while True:
        qual = input("\nQual funcionário deseja analisar? ").capitalize()
        qual = ver(qual, nomes)
        for funcionario in db:
            if qual == funcionario["nome"]:
                if funcionario["CTPS"] != 0:
                    print(f"""
{"-="*30}
    nome: {funcionario["nome"]}
    idade: {funcionario["idade"]}
    CTPS: {funcionario["CTPS"]}
    Contratação: {funcionario["Contratação"]}
    Salário: {funcionario["Salário"]}
    Aposentadoria: {funcionario["Aposentadoria"]} anos
{"-="*30}
                """)
                else:
                    print(f"""
{"-="*30}
    nome: {funcionario["nome"]}
    idade: {funcionario["idade"]}
    CTPS: \033[31mNÃO POSSUI\033[m
{"-="*30}""")
                resp = input("deseja continuar[S/N]? ").upper()
                resp = ver(resp, "SNsn")
                if resp in "Nn":
                    exit(0)
        