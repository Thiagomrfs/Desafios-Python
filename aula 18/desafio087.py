# aprimore a matriz mostrando a soma dos valores pares, a soma da 3º coluna e o maior na linha 2

valores = []
col1 = []
col2 = []
col3 = []
pares = []

for c in range(1, 4):
    num = int(input(f"Insira o valor da posição 1x{c}: "))
    col1.append(num)
    if num % 2 == 0:
        pares.append(num)

for c in range(1, 4):
    num = int(input(f"Insira o valor da posição 2x{c}: "))
    col2.append(num)
    if num % 2 == 0:
        pares.append(num)

for c in range(1, 4):
    num = int(input(f"Insira o valor da posição 3x{c}: ")) 
    col3.append(num)
    if num % 2 == 0:
        pares.append(num)

valores.append(col1)
valores.append(col2)
valores.append(col3)
soma = valores[0][2] + valores[1][2] + valores[2][2]

print(f"""
Sua matriz é:

            [ {valores[0][0]} ] [ {valores[0][1]} ] [ {valores[0][2]} ]
            [ {valores[1][0]} ] [ {valores[1][1]} ] [ {valores[1][2]} ]
            [ {valores[2][0]} ] [ {valores[2][1]} ] [ {valores[2][2]} ]

Os valores pares dessa matriz são: {pares}
A soma dos valores da 3º coluna é: {soma}
O maior valor na 2º linha é: {max(valores[1])}
""")