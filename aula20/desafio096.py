# faça uma funçâo que receba largura e comprimento de uum terreno e calcule a sua área + perímetro
def area():
    larg = int(input("digite a largura do terreno(m): "))
    comp = int(input("digite o comprimento do terreno(m): "))
    print(f"A área é {larg*comp}m²")


area()
