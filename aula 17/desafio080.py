# leia 5 valores numéricos e coloque na posição correta sem usar o sort()
list = []
menor = 0

for c in range(0, 5):
    num = int(input("insira um número: "))
    if c == 0:
        list.append(num)
    else:
        if num < min(list):
            list.insert(list.index(min(list)), num)
        if num > max(list):
            list.insert(list.index(min(list))+1, num)

print(list)