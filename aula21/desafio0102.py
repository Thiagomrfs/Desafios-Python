# crie uma função que calcule o fatorial e tenha um param opcional(lógico) que mostre o processo de calculo

def fat(num, show=False):
    if show == False:
        f = 1
        for n in range(num, 0, -1):
            f *= n
        return f
    else:
        f = []
        mult = 1
        for n in range(num, 0, -1):
            mult *= n
            f.append(str(n))
        return f"{' x '. join(f)} = {mult}"

print(fat(3, True))