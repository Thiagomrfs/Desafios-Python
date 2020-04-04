contmaior = 0
contmenor = 0

for c in range(1, 8):
    year = int(input("Digite o seu ano de nascimento: "))
    age = 2020 - year
    if age >= 21:
        contmaior += 1
    else:
        contmenor += 1
print(f"No grupo de 7 pessoas existem {contmaior} maiores de idade e {contmenor} menores")
