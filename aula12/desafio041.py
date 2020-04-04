# 41 - categorize um atleta pela sua idadde. até 9 anos: mirin / até 14: infantil / até 19: júnior / 20: sênior / + master

idade = int(input("Insira a sua idade: "))

if idade <= 9 :
    print("De acordo com a sua idade você se classifica como mirin")
elif idade > 9 and idade <= 14:
    print("De acordo com a sua idade você se classifica como infantil")
elif idade > 14 and idade <= 19:
    print("De acordo com a sua idade você se classifica como júnior")
elif idade == 20:
    print("De acordo com a sua idade você se classifica como sênior")
else:
    print("De acordo com a sua idade você se classifica como master")