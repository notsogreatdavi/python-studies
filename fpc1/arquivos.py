qt_arq, limite_pasta = map(int, input().split())
arquivos = [] * qt_arq
limite_temp = limite_pasta
contador = 0

arquivos = input().split()
for i in range(len(arquivos)):
    limite_temp -= int(arquivos[i])
    if limite_temp <= 0:
        contador += 1
        limite_temp = limite_pasta

print(contador)