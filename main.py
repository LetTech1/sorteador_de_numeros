import random

quantidadeDeNumeros = int(input('Quantidade de números: '))
minimo = int(input('Do número: '))
maximo = int(input('Até o número: '))
listaNumerosSorteados = []

def sortear(min, max, quantidade):
    while quantidade != 0:
        numeroSorteado = random.randrange(min, max, quantidade)
        if(listaNumerosSorteados.__contains__(numeroSorteado)):
            return sortear(minimo, maximo, quantidadeDeNumeros)
        else:
            listaNumerosSorteados.append(numeroSorteado)
            quantidade = quantidade - 1
    print(listaNumerosSorteados)



sortear(minimo, maximo, quantidadeDeNumeros)



