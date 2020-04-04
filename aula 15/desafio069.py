#leia a idade e o sexo de vériaas pessoas, a cada pessoa cadastrada o programa pergunta se o user quer continuar
#depois mostrre:quantas pessoas tem mais de 18/ quantos homens foram cadastrados/ quantas mulheres tem mais de 20


def ver(x, y):
    if x not in y.split():
        while x not in y:
            x = input("\033[31mCOMANDO INVÁLIDO, POR FAVOR INDIQUE UM VALOR VÁLIDO: \033[m")
    return x


resp = "s"
count = 1
m18 = 0
homem = 0
mulher20 = 0

while resp in "sS":
    print(f"{count}ª pessoa")
    count += 1
    nome = input("Digite o seu nome: ")
    idade = int(input("Indique a sua idade: "))
    if idade > 18:
        m18 += 1
    sexo = input("Indique seu sexo[M/F]: ")
    sexo = ver(sexo, "mFMf")
    if sexo in "Mm":
        homem += 1
    if sexo in "fF" and idade > 20:
        mulher20 += 1
    # continue
    quest = input("Quer continuar[S/N]? ")
    if quest in "sS":
        resp = "s"
    elif quest in "nN":
        break
    else:
        resp = ver(quest, "sSnN")

print(f"No espaço amostral existem {m18} pessoas maiores de 18 anos, {mulher20} mulheres acima de 20 anos e"
      f" {homem} homens cadastrados")
