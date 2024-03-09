def quick_sort(sequencia):
    tamanho = len(sequencia)
    if tamanho <= 1:
        return sequencia
    else:
        pivo = sequencia.pop()

    items_maior = []
    items_menor = []

    for item in sequencia:
        if item > pivo:
            items_maior.append(item)
        else:
            items_menor.append(item)
    return quick_sort(items_menor) + [pivo] + quick_sort(items_maior)

print(quick_sort([3, 4, 5, 6, 2, 7]))
