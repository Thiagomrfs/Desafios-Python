#mostre o seno, cosseno e tangente de um ângulo
import math

ang = float(input("Digite o valor do ângulo desejado: "))

print(f"Para o ângulo {ang}°, temos {math.cos(math.radians(ang)):.2f} como cosseno, {math.sin(math.radians(ang)):.2f}"
      f" como seno e {math.tan(math.radians(ang)):.2f} como tangente.")