# use o interactive help do python e use cores, quando ele digitar fim encerre

def msg(text):
    print("\033[32m"+"="*len(text))
    print(text)
    print("="*len(text)+"\033[m")

while True:
    msg("sistema de ajuda python")
    help(input("\033[34minsira o comando que deseja procurar:\033[36m "))
    resp = input("\033[35mDeseja continuar? [S/N] ").upper()
    if resp == "N":
        break