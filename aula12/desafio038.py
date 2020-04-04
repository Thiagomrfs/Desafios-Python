n1 = int(input("Insira um número: "))
n2 = int(input("Insira outro: "))

if n1>n2:
    print(f"O número \033[35m{n1}\033[m é maior.")
elif n1 == n2:
    print("os dois números \033[31msão iguais")
else:
    print(f"O número \033[36m{n2}\033[m é maior")