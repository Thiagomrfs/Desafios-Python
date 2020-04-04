#leia um número real e mostre na tela a sua porção inteira
import math

num = float(input("Digite um número: "))
inteiro = math.trunc(num)

print(f'A porção inteira desse número é {inteiro}')