# melhore o desafio 61 perguntando se ele quer ver mais alguns termos, depois para quando ele quiser parar
# leia a razão e o primeiro termo de uma PA e faça eus 10 primeiros termos usando while
a1 = int(input("Digite o primeiro termo da P.A: "))
r = int(input("Digite a razão da P.A: "))

an = a1 + (9*r)
print(f"O décimo termo dessa P.A. é: {an}")
resp = input("Deseja continuar[S/N]: ").upper()
while resp != "N":
    qnt = int(input("Quantos números a mais você quer? "))
    for c in range(qnt):
        seg = an + r
        an = seg
        print(an)
    resp = input("Deseja continuar[S/N]: ").upper()
