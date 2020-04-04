# leia um num (n) inteiro e mostre na tela os n primeiros elementos de uma sequencia de fibonacci
n = int(input("Digite um número: "))
fb = 0
a1 = 0
a2 = 1
count = 0

while count < n:
    count += 1
    fb = a1 + a2
    a1 = a2
    a2 = fb
    print(a1, end=" ")