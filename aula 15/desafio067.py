# faça um programa que mostre a tabuada de vários números q o usuário botar: pare quando ele digitar um negativo
num = 1

while num > 0:
    num = int(input("Digite um número: "))
    if num < 0:
        break
    else:
        print("-="*30)
        for c in range(1, 11):
            print(f"{num} multiplicado por {c} é {num*c}")
        print("-="*30)
print("Obrigado por utilizar o nosso sistema!")