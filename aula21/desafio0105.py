# programa notas() q recebe várias notas de alunos e crie um dic com as seguintes informações:
# quantidade de notas, maior, menor, média e situação(opcional), adicione também a docstring

def notas(*notas, sit=False):
    situation = ''
    quant = len(notas)
    maior = max(notas)
    menor = min(notas)
    soma = 0
    for nota in notas:
        soma += nota
    med = soma/quant

    if sit == True:
        if med <= 5:
            situation = "ruim"
        elif med == 6:
            situation = "regular"
        else:
            situation = "boa"
        print(f'''
        quantidade de notas = {quant}
        max = {maior}
        min = {menor}
        média = {med}
        situação = {situation}
        ''')
    else:
        print(f'''
        quantidade de notas = {quant}
        max = {maior}
        min = {menor}
        média = {med}
        ''')




notas(2, 5, 8, 1, 2, sit=True)
notas(2, 5, 8, 1, 2)
notas(5, 7, 2, 5, 4)
notas(2, 4, 6, sit=True)