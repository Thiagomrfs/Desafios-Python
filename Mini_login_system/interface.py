import suporte
import cadastro
import Listagem

resp = 0
continuar = ""

suporte.msg("Bem vindo ao Cadastro de funcionários Marinho Ltda.", 32)
while True:
    print("""\033[36m===================================================\033[m
        Indique a operção desejada:

    1 - Cadastrar novo funcionário
    2 - Listar os funcionários cadastrados
    3 - Encerrar o sistema

\033[36m===================================================\033[m
    """)

    resp = suporte.verificarInt(resp, [1, 2, 3])
    if resp == 1:
        cadastro.cadastrar()
    elif resp == 2:
        Listagem.ler_data()
    elif resp == 3:
        exit()
    
    continuar = suporte.verificarSN(continuar)
    if continuar == "N":
        exit()
    print()