num = int(input("Digite um número: "))
resp = 0

for c in range(1, num+1):
    if num % c == 0:
        print("\033[34m", end=" ")
        resp += 1
    else:
        print("\033[31m", end=" ")
    print(f"{c}", end=" ")

if resp == 2:
    print(f"\n\033[34mseu número É primo")
else:
    print("\n\033[31mseu número NÃO é primo!")
