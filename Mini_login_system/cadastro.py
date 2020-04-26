import sys

def cadastrar():
    print("-"*10+" Cadastrando novo funcionário "+"-"*10)
    funcionário = input("Insira o nome do funcionário: ").title()
    cargo = input("Insira o cargo que este funcionário ocupa: ").capitalize()
    arquivo = open("database.txt", "a+")
    arquivo.write(f"{funcionário.ljust(30,'.')} {cargo}\n")
    arquivo.close()

if __name__ == "__main__":
    cadastrar()