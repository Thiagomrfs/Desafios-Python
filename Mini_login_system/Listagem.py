import sys

def ler_data():
    arquivo = open("database.txt")
    # Pode ser uma opção
    # for linha in arquivo: 
    #     sys.stdout.write(linha)
    print("-="*35)
    print()
    print("\033[36m"+"funcionário".ljust(30), "Função"+"\033[m")
    print("".join(arquivo.readlines()))
    print("-="*35)
    print()
    arquivo.close()

if __name__ == "__main__":
    ler_data()