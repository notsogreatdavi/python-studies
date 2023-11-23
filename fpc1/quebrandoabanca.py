resultados = []
def max_num(a, b, valor):
    saldo_temp = []

    for caracter in valor:
        while b > 0 and saldo_temp and saldo_temp[-1] < caracter:
            saldo_temp.pop()
            b -= 1
        saldo_temp.append(caracter)

    while b > 0:
        saldo_temp.pop()
        b -= 1
    return ''.join(saldo_temp)

while True:
    try:
        a, b = map(int, input().split())
        valor = input().strip()

        resultado = max_num(a, b, valor)
        resultados.append(resultado)

    except EOFError:
        for elem in resultados:
            print(elem)
        break