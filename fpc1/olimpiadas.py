N, M = map(int, input().split())

def organizar_classificacao(paises, modalidades):
    medalhas = {i: [0, 0, 0] for i in range(1, paises + 1)}

    for i in range(modalidades):
        ouro, prata, bronze = map(int, input().split())
        medalhas[ouro][0] += 1
        medalhas[prata][1] += 1
        medalhas[bronze][2] += 1

    def pontuacao(pais):
        ouro, prata, bronze = medalhas[pais]
        return (-ouro, -prata, -bronze, pais)

    def quicksort(array):
        if len(array) <= 1:
            return array
        else:
            pivo = array[0]
            menores = [item for item in array[1:] if pontuacao(item) < pontuacao(pivo)]
            maiores = [item for item in array[1:] if pontuacao(item) >= pontuacao(pivo)]
            return quicksort(menores) + [pivo] + quicksort(maiores)
    
    classificacao = quicksort(list(medalhas.keys()))

    return classificacao

classificacao_final = organizar_classificacao(N, M)

print(*classificacao_final)
