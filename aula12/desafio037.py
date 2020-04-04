num = int(input("Insira um número inteiro: "))
print("""Escolha a conversão:
1 ) BINÁRIO
2 ) OCTAL
3 ) HEXADECIMAL""")
opc = int(input("Opção: "))
if opc == 1:
    print(f"o número em binário é: {bin(num)}")
elif opc == 2:
    print(f"o número em octal é: {oct(num)}")
elif opc == 3:
    print(f"O número em hexadecimal é: {hex(num)}")
else:
    print("Comando inválido")