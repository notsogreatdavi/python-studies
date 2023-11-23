arq = open("pisi2/input.txt", "r")
listalinhas = arq.readlines()
arq.close()
linha_coluna = listalinhas[0].split()
matriz = [""] * int(linha_coluna[0])
paths = []
pontos = {}
distancias = {}
caminhos_dist = {}

for i in range(1, int(linha_coluna[1])):
    matriz[i-1] = listalinhas[i].split()

for i, linha in enumerate(matriz):
   for j, elemento in enumerate(linha):
       if elemento != "0":
           pontos[elemento] = (i, j)

for chave in pontos:
    for chave2 in pontos:
        distancias[chave + chave2] = abs(pontos[chave][0] - pontos[chave2][0]) + abs(pontos[chave][1] - pontos[chave2][1])
           
def permutacoes(s):
  if len(s) == 1:
      return [s]

  permuta = []
  for i in range(len(s)):
      resto = s[:i] + s[i+1:]
      for p in permutacoes(resto):
          permuta.append(s[i:i+1] + p)
  return permuta

pontos_nomes = list(pontos.keys())
str_pontos = ""
for i in range(len(pontos_nomes)):
    if str(pontos_nomes[i]) != "R":
        str_pontos += str(pontos_nomes[i])
caminhos = permutacoes(str_pontos)

for elem in caminhos:
    distancia_percorrida = 0
    for i in range(len(elem) - 1):
        elem = "R" + elem + "R"
        if elem[i:i+2] in distancias:
            distancia_percorrida += distancias[elem[i:i+2]]
            caminhos_dist[elem] = distancia_percorrida

caminhos_dist_ord = dict(sorted(caminhos_dist.items(), key=lambda item: item[1]))
caminhos_ord = list(caminhos_dist_ord.keys())
print(caminhos_ord[0])