# 43 - calcule o IMC de uma pessoa e categorize. -18.5 = abaixo do peso / 18.5~25 = ideal / 25~30 = sobrepeso
# 30~40 = obesidade / +40 = obesidade mórbida.

peso = int(input("Insira  seu peso: "))
heigth = int(input("Insira a sua altura: "))
IMC = peso/heigth**2

if IMC <= 18.5:
    print("Você está abaixo do peso")
elif 18.5 < IMC <= 25:
    print("Você está no peso ideal")
elif 25 < IMC <= 30:
    print("Você está acima do peso")
elif 30 < IMC <= 40:
    print("Você está com obesidade")
elif 40 < IMC:
    print("Você está com obesidade mórbida")