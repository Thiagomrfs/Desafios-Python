# leia o nome, sexo e idade de várias pessoas, guarde as pessoas num dic e todos os dics numa lista e mostre:
# Qunatas pessoas fora cadastradas; a média de idade do grupo; uma lista com todas as mulheres; uma lista com as pessoas de idade acima da média
def ver(x, y):
    if x not in y:
        while x not in y:
            x = input("\033[31mCOMANDO INVÁLIDO, POR FAVOR INSIRA UM VALOR VÁLIDO: \033[m").capitalize()
    return x


db = []
count = 0
molieres = []
somaIdade = 0

while True:
    aux = {}
    print(f"{'< '+str(count+1)+'º pessoa >':-^30}")
    aux['nome'] = input("insira o seu nome: ").capitalize()
    aux['sexo'] = input("insira o seu sexo: [M/F] ").upper()
    if aux['sexo'] == "F":
        molieres.append(aux['nome'])
    aux['idade'] = int(input("insira a sua idade: "))
    count += 1
    somaIdade += aux['idade']
    db.append(aux)
    resp = input("deseja continuar[S/N]? ").capitalize()
    resp = ver(resp, "SNsn")
    if resp in "Nn":
        break
    print()

med = somaIdade/count
acima_med = []
for pessoa in db:
    if pessoa['idade'] < med:
        acima_med.append(pessoa['nome'])

print(f"""
-> Quantidade de pessoas cadastradas: {count}
-> Mulheres cadastradas: {', '.join(molieres)}
-> Média de idade do grupo: {med}
-> Pessoas que tem idade acima da média: {', '.join(acima_med)} 

\033[34mOBRIGADO POR UTILIZAR O NOSSO SISTEMA!!!\033[m
""")