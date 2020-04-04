# leia 3 número e mostre qual o maior e menor
a = float(input("Digite um número: "))
b = float(input("Outro: "))
c = float(input("Outro: "))

if a > b and a > c:
    maior = a
elif b > a and b > c:
    maior = b
elif c > a and c > b:
    maior = c
if a < b and a < c:
    menor = a
elif b < a and b < c:
    menor = b
elif c < a and c < b:
    menor = c

print(f"\nDentre os 3 números indicados {maior} é o maior e {menor} é o menor.")