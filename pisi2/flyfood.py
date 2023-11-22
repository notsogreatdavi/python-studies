arq = open("pisi2/input.txt", "r")
listalinhas = arq.readlines()
arq.close()
linha_coluna = listalinhas[0].split()
matriz = [""] * int(linha_coluna[0])

for i in range(1, int(linha_coluna[1])):
    matriz[i-1] = listalinhas[i].split()


print(matriz)

# Calcular a distância de cada ponto para os outros pontos
# Criar todas as possibilidade possíveis com os caminhos que foram dados e formar um caminho com cada um
# Calcular a distância percorrida por cada um dos caminhos
# Comparar os caminhos e printar o menor