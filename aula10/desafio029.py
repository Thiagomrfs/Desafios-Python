# leia a velocidade de um carro e adicione multas de 7 reais para cada km acima de 80km/h
vel = int(input("\033[35mDigite a velocidade do carro: \033[m"))
if vel < 80:
    print("\033[32mA sua velocidade está dentro dos padrões, continue assim.")
else:
    print(f"\033[31mA sua velocidade excedeu o limite em {vel - 80} km/h, você receberá uma multa de {(vel - 80)*7} reais.")
print("\033[36mObrigado por utilizar o nosso sistema.")