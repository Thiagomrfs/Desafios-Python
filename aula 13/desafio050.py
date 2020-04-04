par = 0

for c in range(1,7):
    num = int(input("Digite o número:"))
    if num % 2 == 0:
        par += num
print(f"The sum of these numbers is {par}")