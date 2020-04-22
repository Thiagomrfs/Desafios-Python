# crie uma funão que receba um texto como parametro e crie um enfeite adaptável ao tamanho da msg
def msg(text):
    print("="*len(text))
    print(text)
    print("="*len(text))

while True:
    phrase = input("insira o texto desejado (STOP para): ")
    if phrase.upper() == "STOP":
        break
    msg(phrase)