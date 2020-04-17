# leia nome e duas notas de vários alunos. mostre um boletim com a média e permita que o usuário possa
# mostrar as notas de cada aluno individualmente
def ver(x, y):
    if x not in y:
        while x not in y:
            x = input("\033[31mCOMANDO INVÁLIDO, POR FAVOR INSIRA UM VALOR VÁLIDO: \033[m").capitalize()
    return x

alunosdb = []
count = 1
while True:
    print("-="*11, f"< {count}º aluno >", "-="*11)
    aluno = input("Insira o nome do aluno: ").capitalize()
    nota1 = float(input("Insira a 1º nota do aluno: "))
    nota2 = float(input("Insira a 2º nota do aluno: "))
    alunosdb.append([aluno, nota1, nota2])
    resp = input("deseja continuar[S/N]? ").upper()
    print()
    resp = ver(resp, "SNsn")
    count += 1
    if resp in "Nn":
        break

print("-="*10, "< médias >", "-="*10)
for a in alunosdb:
    media = (a[1] + a[2])/2
    if media >= 6:
        print(f'\033[32m{a[0]:.<25}'+ f" {media}\033[m")
    else:
        print(f'\033[31m{a[0]:.<25}'+ f" {media}\033[m")
        
ask = input("Deseja consultar as notas individuais de algum aluno?[S/N] ").upper()
ask = ver(ask, "SNsn")

if ask in "Ss":
    nomes = []
    for aluno in alunosdb:
        nomes.append(aluno[0])
    while True:
        qual_aluno = input("Qual aluno deseja analisar? ").capitalize()
        qual_aluno = ver(qual_aluno, nomes).capitalize()
        for aluno in alunosdb:
            if qual_aluno == aluno[0]:
                print(f"""
    Aluno {aluno[0]}:
            Nota 1: {aluno[1]}
            Nota 2: {aluno[2]}
            Média: {(aluno[1] + aluno[2]) / 2}
                """)
        resp = input("deseja continuar[S/N]? ").upper()
        resp = ver(resp, "SNsn")
        if resp in "Nn":
            print("OBRIGADO POR UTILIZAR O NOSSO SISTEMA!")
            break
else:
    print("OBRIGADO POR UTILIZAR O NOSSO SISTEMA!")
