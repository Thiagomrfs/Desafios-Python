#leia o cateto oposto e o adjacente e dê a hipotenusa
import math

CO = float(input("Digite o valor do cateto oposto: "))
CA = float(input("Digite o valor do cateto adjacente: "))

print(f"A hipotenusa desse triangulo retângulo é {math.hypot(CA, CO)}")