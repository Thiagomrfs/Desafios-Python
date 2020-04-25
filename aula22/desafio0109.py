# modifique as func do 107 para que aceite um param a mais informando se o valor dela vai ou não ser formatado
# pela função moeda

from utilidadesCev import moeda
from utilidadesCev import dados

num = float(dados.verifica_num(input("Insira um valor: ")))
print(f"O valor {moeda.formatado(num)} dobrado é: "+moeda.dobro(num, True))
print(f"O valor {moeda.formatado(num)} adicionando 10% é: "+moeda.adicionar(num, 10, True))
print(f"O valor {moeda.formatado(num)} diminuindo 10% é: "+moeda.diminuir(num, 10, True))
print(f"O valor {moeda.formatado(num)} pela metade é: "+moeda.metade(num, True))
