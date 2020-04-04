# leia o peso de 5 pessoas e diga o maior e o menor
maior = 0
menor = 0

for c in range(1, 6):
    peso = float(input("digite o seu peso: "))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        elif peso < menor:
            menor = peso

print(f"O menor é {menor} e o maior é {maior}")