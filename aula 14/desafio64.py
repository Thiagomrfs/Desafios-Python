# leia vários numeros inteiros e pare quando o usuário digitar 999
#depois mostre a quantidade de números e a soma entre eles(desconsiderando o flag)
sum = 0
count = 0
resp = ""
while resp != "N":
    print("ATENÇÃO! Digite o número 999 para parar o programa")
    n = int(input("Digite um número inteiro: "))
    count += 1
    sum += n
    if n == 999:
        resp = input("Deseja continuar[S/N]? ").upper()
count = count - 1
sum = sum - 999
print(f"Você inseriu {count} números e a soma entre eles é: {sum}")