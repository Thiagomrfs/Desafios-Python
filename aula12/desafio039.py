# 39 - leia o ano de nascimento de alguém e diga se ela ainda vai se alistar, se é a hora de se alistar ou se já passou
# do tempo de
# se alistar. o programa também deverá informar quanto tempo passou ou falta para o alistamento
from datetime import datetime

ano = int(input("Digite o seu ano de nascimento: "))
now = datetime.now()
idade = int(now.year) - ano

if idade == 18:
    print("Você deve se alistar imediatamente.")
elif idade > 18:
    print(f"Você devia ter se alistado a {idade - 18} anos")
else:
    print(f"Você irá se alistar em {18 - idade} anos")