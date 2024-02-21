def calcular_distancia(ponto1, ponto2):
    return abs(ponto1[0] - ponto2[0]) + abs(ponto1[1] - ponto2[1])

def mais_proximo(posicoes_letras, ponto_inicial):
    pontos_restantes = list(posicoes_letras.keys())
    pontos_restantes.remove(ponto_inicial)

    ponto_atual = ponto_inicial
    caminho = [ponto_atual]

    while pontos_restantes:
        distancias = {ponto: calcular_distancia(posicoes_letras[ponto_atual], posicoes_letras[ponto]) for ponto in pontos_restantes}
        ponto_mais_proximo = min(distancias, key=distancias.get)

        caminho.append(ponto_mais_proximo)
        ponto_atual = ponto_mais_proximo
        pontos_restantes.remove(ponto_mais_proximo)

    # Retornar ao ponto R 
    caminho.append(ponto_inicial)

    return caminho

arq = open("input.txt", "r")
listalinhas = arq.readlines()
arq.close()

linha_coluna = listalinhas[0].split()
matriz = [""] * int(linha_coluna[0])
pontos = {}

for i in range(1, int(linha_coluna[0]) + 1):
    matriz[i-1] = listalinhas[i].split()

for i, linha in enumerate(matriz):
    for j, elemento in enumerate(linha):
        if elemento != "0":
            pontos[elemento] = (i, j)

caminho_proximo = mais_proximo(pontos, 'R')

# Distância total do caminho encontrado
distancia_total = sum(calcular_distancia(pontos[caminho_proximo[i]], pontos[caminho_proximo[i+1]]) for i in range(len(caminho_proximo)-1))
print(caminho_proximo, "Distância do caminho:",distancia_total)
