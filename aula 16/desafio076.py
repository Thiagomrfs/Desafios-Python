# crie uma tupla única com o nome do produto e o preço na sequencia, depois mostre uma tabulação de produto-preço
tup = ("carrinho", 9.00, "ventilador", 530.50, "televisão", 1500, "computador", 2600, "pc gamer", 3400, "mouse gamer",
       9999.99)

print("       TABELÃO DE PREÇOS")
for c in range(0, len(tup)+1):
    if c % 2 == 0 and c+1 < len(tup) + 1:
        print(f"{tup[c].ljust(30, '.' )} R$ {tup[c + 1]:.2f}")