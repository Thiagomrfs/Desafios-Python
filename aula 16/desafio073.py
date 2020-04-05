# pegue uma tabela com os 20 colocados do campeonato brasileiro de fut e depois mostre:
# 5 primeiros, 5 ultimos, times em ordem alfabética, where is chapecoense

bras = ("Flamengo", "Santos", "Palmeiras", "Grêmio", "Atlético - PR", "São Paulo", "Internacional", "Corinthians",
        "Fortaleza", "Goiás", "Bahia", "Vasco", "Atlético - MG", "Fluminense", "Botafogo", "Ceará", "Cruzeiro",
        "CSA", "Chapecoense", "Avaí")

first5 = bras[:5]
last5 = bras[16:]
OA = sorted(bras)
chape = bras.index("Chapecoense")

print(f"""
os 5 primeiros são: {first5}
os 5 ultimos são: {last5}
em ordem alfabética: {OA}
chapecoense está na {chape+1} colocação
""")