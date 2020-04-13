# leia 5 valores numéricos e coloque na posição correta sem usar o sort()
list = []
menor = 0

for c in range(0, 5):
    num = int(input("insira um número: "))
    if c == 0:
        list.append(num)
    else:
        if num >= max(list):
            list.append(num)
        elif num <= min(list):
            list.insert(0, num)
        elif min(list) < num < max(list):
            if num < list[1]:
                list.insert(1, num)
            elif list[1] < num < list[2]:
                list.insert(2, num)
            elif list[2] < num < list[3]:
                list.insert(3, num)


print(list)