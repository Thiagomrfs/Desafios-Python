# tenha uma função chamada voto e receba o ano de nascimento de alguém e vai retornar um valor literal dizendo
# se essa pessoa tem voto negado, opcional ou aprovado
from datetime import datetime

def voto(ano):
    id = datetime.now().year - ano
    if 16 <= id <= 17 or id > 64:
        return "OPICIONAL"
    elif id < 16:
        return "NEGADO"
    else:
        return "APROVADO"


situation = voto(int(input("Insira o seu ano de nascimento: ")))
print(f"Sua situação é {situation}")