# crie uma matriz 3x3 e a complete com os valores lidos no teclado, depois mostre a matriz com a formatação
# correta
valores = []
col1 = []
col2 = []
col3 = []

for c in range(1, 4):
    num = int(input(f"Insira o valor da posição 1x{c}: "))
    col1.append(num)

for c in range(1, 4):
    num = int(input(f"Insira o valor da posição 2x{c}: "))
    col2.append(num)

for c in range(1, 4):
    num = int(input(f"Insira o valor da posição 3x{c}: ")) 
    col3.append(num)

valores.append(col1)
valores.append(col2)
valores.append(col3)

print(f"""
Sua matriz é:

            [ {valores[0][0]} ] [ {valores[0][1]} ] [ {valores[0][2]} ]
            [ {valores[1][0]} ] [ {valores[1][1]} ] [ {valores[1][2]} ]
            [ {valores[2][0]} ] [ {valores[2][1]} ] [ {valores[2][2]} ]

""")