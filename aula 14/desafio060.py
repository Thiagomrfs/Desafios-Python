# leia um número qualquer e faça o seu fatorial
n = int(input("Digite o número: "))
c = n
ft = 1

while c > 1:
    ft *= c
    c -= 1
    print(ft)
