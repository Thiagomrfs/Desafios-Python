#faz uma tupla com várias palavras sem acento e mostre pra cada palavra suas vogais
tup = ("futuro", "jogo", "bala", "transformer", "naruto", "anime", "celeste", "shitpost", "pixel")

for c in tup:
    vogais = []
    for letra in c:
        if letra in "aeiouAEIOU":
            vogais.append(letra)
    print(f"{c.upper()}   possi as vogais   {', '.join(vogais)}")