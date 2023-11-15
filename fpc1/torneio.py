resultados = []
vitorias_cont = 0

for i in range(6):
    resultados.append(input("Digite o resultado de seus jogos em ordem, um por vez em cada linha, sendo V vitória e P perda\n"))

for i in range(len(resultados)):
    if resultados[i] == 'v' or resultados[i] == 'V':
        vitorias_cont += 1

if vitorias_cont == 5 or vitorias_cont == 6:
    print(1)
elif vitorias_cont == 3 or vitorias_cont == 4:
    print(2)
elif vitorias_cont == 1 or vitorias_cont == 2:
    print(3)
else:
    print(-1)