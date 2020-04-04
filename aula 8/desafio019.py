# sorteie entre 4 alunos e selecione 1
import random

a1 = input("Digite o nome do aluno 1: ")
a2 = input("Digite o nome do aluno 2: ")
a3 = input("Digite o nome do aluno 3: ")
a4 = input("Digite o nome do aluno 4: ")

lista = [a1, a2, a3, a4]
esc = random.choice(lista)

print(f"O alundo escolhido foi \033[31m{esc}")