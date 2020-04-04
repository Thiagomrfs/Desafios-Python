# leia o nome de uma cidade e veja se ela começa com a palavra santo(são)
# var.split[0] / "santo" in var
city = input("Digite o nome de uma cidade: ")
div = city.split()
resp = "São" in div[0].capitalize()
print(f"A sua cidade começa com santo (São)? \033[4;34m{resp}")