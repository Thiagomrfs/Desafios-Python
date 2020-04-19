# aprimore o 93 para que ele funcione para vários jogadores,
# incluindo um sistema de visualização do aproveitamento de cada jogador

def ver(x, y):
    if x not in y:
        while x not in y:
            x = input("\033[31mCOMANDO INVÁLIDO, POR FAVOR INSIRA UM VALOR VÁLIDO: \033[m").capitalize()
    return x


db = []
count = 0
jogadores = []

while True:
    jogador = {}
    print(f"{'< '+str(count+1)+'º jogador >':-^30}")
    jogador['nome'] = input("insira o seu nome: ").capitalize()
    jogador["quant"] = int(input("Insira a quantidade de partidas disputadas: "))

    aux = {}    #recebe a quantidade de gols em cada partida
    gols = 0
    for c in range(1, jogador['quant']+1):
        aux[f"partida {c}"] = int(input(f"Insira a quantidade de gols realizados na partida {c}: "))
        gols += aux[f"partida {c}"]
    jogador["partidas"] = aux
    jogador["gols"] = gols

    db.append(jogador)
    jogadores.append(jogador['nome'])
    count += 1

    resp = input("deseja continuar[S/N]? ").capitalize()
    resp = ver(resp, "SNsn")
    print()
    if resp in "Nn":
        break

resp = input("deseja analisar algum dado?[S/N]? ").capitalize()
resp = ver(resp, "SNsn")
if resp == "S":
    while True:
        qual_jogador = input("Qual jogador deseja analizar? ").capitalize()
        qual_jogador = ver(qual_jogador, jogadores)
        for atleta in db:
            if qual_jogador == atleta['nome']:
                print(f"""\033[37m
                Jogador: {atleta["nome"]}
                Partidas: {atleta["quant"]} partidas
                Gols no campeonato: {atleta["gols"]} gols
                \033[m""")
        resp = input("deseja continuar[S/N]? ").capitalize()
        resp = ver(resp, "SNsn")
        if resp in "Nn":
            print()
            print("OBRIGADO POR UTILIZAR O NOSSO SISTEMA!")
            break
else:
    print()
    print("OBRIGADO POR UTILIZAR O NOSSO SISTEMA!")