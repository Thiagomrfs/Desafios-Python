# adapte o 107 para mostrar os valores monetários formatados
from utilidadesCev import moeda
from utilidadesCev import dados

num = float(dados.verifica_num(input("Insira um valor: ")))
print(f"O valor {moeda.formatado(num)} dobrado é: "+moeda.formatado(moeda.dobro(num)))
print(f"O valor {moeda.formatado(num)} adicionando 10% é: "+moeda.formatado(moeda.adicionar(num, 10)))
print(f"O valor {moeda.formatado(num)} diminuindo 10% é: "+moeda.formatado(moeda.diminuir(num, 10)))
print(f"O valor {moeda.formatado(num)} pela metade é: "+moeda.formatado(moeda.metade(num)))
