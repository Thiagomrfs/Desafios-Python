# aumento para os funcionários: para salarios superiores a 1250 +10% e menor ou igual +15%
sal = float(input("Digite o seu salário: "))
if sal <= 1250:
    print(f"O reajuste no seu salário será de 15%, assumindo o valor de: {sal + (15/100*sal)}")
else:
    print(f"O reajuste no seu salário será de 10%, assumindo o valor de: {sal + (10/100*sal)}")
print("obrigado por uitlizar o nosso sistema".upper())