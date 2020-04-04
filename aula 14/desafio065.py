# leia vários números inteiros e no final mostre a média entre todos os valores
# e o maior e o menor valores lidos. Pergunte se o cara quer continuar.
resp = ""
count = 0
sum = 0
maior = 0
menor = 0

while resp != "N":
    n = int(input("Digite um número: "))
    count += 1
    sum += n
    resp = input("Você que continuar[S/N]? ").upper()
    if count == 1:
        maior = n
        menor = n
    else:
        if n > maior:
            maior = n
        elif n < menor:
            menor = n

med = sum/count
print(f"A média entre os seus valores é: {med}")
print(f"O maior valor é {maior} e o menor valor é {menor}")
