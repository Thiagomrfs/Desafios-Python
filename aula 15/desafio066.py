# crie um programa que leia vários números inteiros pelo teclado e pare quando o usuário digitar 999 e moste
# quantos numeros e a soma sem o flag
inf = 1
count = 0
sum = 0

while inf != 2:
    num = int(input("Digite um número "))
    if num == 999:
        break
    else:
        count += 1
        sum += num
print(f"Você digitou {count} números e a soma deles é: {sum}")