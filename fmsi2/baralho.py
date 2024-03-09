import random

def criar_baralho():
    # cria as cartas de maneira numérica no baralho, cartas de 2 a 10, cada uma 4 vezes pra cada naipe
    baralho = [value for value in range(2, 11) for _ in range(4)]

    # adicionas os ases: 4 cartas, cada uma valendo 1
    baralho += [1] * 4

    # adiciona as cartas (J, Q, K): 12 cartas, cada uma valendo 10
    baralho += [10] * 12

    return baralho

def simulacao(rodadas=100000):
    contador = 0

    for i in range(rodadas):
        baralho = criar_baralho()
        random.shuffle(baralho)
        mao = random.sample(baralho, 3)

        if sum(mao) == 21:
            contador += 1

    probabilidade = contador / rodadas
    return probabilidade

probabilidade = simulacao()
print(f"A probabilidade de que a soma de três cartas seja 21 é aproximadamente {probabilidade:.4f} ou {probabilidade*100:.2f}%.")
