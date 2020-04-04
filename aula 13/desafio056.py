#  leia nome idade e sexo de cada pessoa e mostre: média de idade do grupo, o nome do homem mais velho e quantas
#  mulheres tem menos de 20 anos
count = 0
somaid = 0
hvelho = ""
mulheres = 0
maioridade = 0

for c in range(1, 6):
    nome = str(input(f"Digite o nome da {c}° pessoa: "))
    idade = int(input(f"Digite a idade da {c}° pessoa: "))
    sexo = str(input(f"Digite o sexo da {c}° pessoa: "))
    count += 1
    if c == 1:
        somaid = idade
    else:
        somaid = somaid + idade
    if sexo == "feminino" and idade >= 20:
        mulheres += 1
    if sexo == "masculino":
        if c == 1:
            hvelho = nome
            maioridade = idade
        else:
            if idade > maioridade:
                hvelho = nome
                maioridade = idade

midade = somaid / count
print(f"A média de idade do grupo é {midade}")
print(f"A quantidade de mulheres acima de 20 anos no grupo é: {mulheres}")
print(f"Com {maioridade} anos, {hvelho} é o homem mais velho.")
