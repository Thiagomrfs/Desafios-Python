import math
sum = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont = cont + 1 # cont += 1
        sum = sum + c # sum += c
print(f"The sum of these {cont} numbers is {sum}.")