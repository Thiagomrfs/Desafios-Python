# 36 - pergunte o valor de uma casa, o salário do interessado e em quantos anos ele irá pagar.
# a prestação mensal não pode exceder 30% do salário do interessado ou o empréstimo é negado.

house = int(input("Digite o valor da casa: R$"))
sal = int(input("Digite o salário do interessado: R$"))
time = int(input("Em quantos anos irá pagar? "))
meses = time*12
PM = house/meses

if PM < 0.30*sal:
    print("\033[4;32mSeu empréstimo foi aprovado!!!")
else:
    print("\033[4;31mSeu empréstimo foi negado.")