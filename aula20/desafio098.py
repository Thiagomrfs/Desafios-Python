# faça uma função cont que receba os param inicio fim e passo e realize a contagem, deve fazer 3 contaggens:
# de 1 até 10 de 1 em 1; 10 até 0 de 2 em 2; uma personalizada. trate os parametros passados:
# se o cara botar inicio maior que o fim, se ele botar passo negativo ou zero

def cont(inicio, fim, passo):
    if inicio > fim:
        print(f"\nDe {inicio} até {fim} de {passo} em {passo}")
        for c in range(inicio, fim-1, -passo):
            print(    c, end=" ")
    elif passo < 0:
        print(f"\nDe {fim} até {inicio} de {-passo} em {-passo}")
        for c in range(inicio, fim+1, passo):
            print(    c, end=" ")
    elif passo == 0:
        print("\nNão é possível realizar a contagem de 0 em 0")
    else:
        print(f"\nDe {inicio} até {fim} de {passo} em {passo}")
        for c in range(inicio, fim+1, passo):
            print(    c, end=" ")

cont(1,10,1)
cont(10,0,2)
i = int(input("\nInsira o número inicial: "))
f = int(input("Insira o número final: "))
p = int(input("Insira o passo: "))
cont(i, f, p)