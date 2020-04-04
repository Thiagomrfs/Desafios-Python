# leia um número de 0 a 9999 e separe os algarismos por unidade, dezena, centena e milhar
#spit / print(var.split[0]) / print(var.split[1]) ...
var = input("Digite um número de 1000 a 9999: ")
print(f"""\nOs dados do seguinte número são:\033[36m
milhar: {var[0]}
centena: {var[1]}
dezena: {var[2]}
unidade: {var[3]}""")

# mission complete