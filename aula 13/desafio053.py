pal = str(input("Digite a sua palavra: "))
var = pal.replace(" ", "").lower()
inv = var[::-1]

if var == inv:
    print("\033[34mÉ UM PALÍNDROMO")
else:
    print("\033[31mNÃO É UM PALÍNDROMO")