# leia a distancia de uma viagem e diga quanto vai custar
# 0,50 reais para viagens de até 200 km e 0,45 para viagem mais longas (por km)
dis = float(input("Digite a distância da viagem: "))
if dis <= 200:
    print(f"O preço a pagar pela viagem é {dis*0.5}")
else:
    print(f"O preço a pagar pela viagem é {dis*0.45}")
print('\033[36m'+"Obrigado por utilizar o nosso sistema!!!".upper())