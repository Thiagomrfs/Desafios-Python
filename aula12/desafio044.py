# 44 - calcule o preço de um produto e a condição. à vista dinheiro/cheque = -10% / à vista cartão = -5%
# 2x no cartão = preço normal / 3x no cartão ou + = 20% de juros
price = int(input("Insira o preço do produto: "))
print("""Escolha a condição: 
1 ) à vista (dinheiro/cheque)
2 ) à vista (cartão)
3 ) 2x no cartão
4 ) 3x ou mais no cartão""")
opc = int(input("Selecione a opção: "))

if opc == 1:
    print(f"O preço nessa condição é de: {price - (0.10*price)}")
elif opc == 2:
    print(f"O preço nessa condição é de: {price - (0.05*price)}")
elif opc == 3:
    print(f"O preço nessa condição é de: {price}")
elif opc == 4:
    print(f"O preço nessa condição é de: {price + (0.20*price)}")
else:
    print("Invalid option")