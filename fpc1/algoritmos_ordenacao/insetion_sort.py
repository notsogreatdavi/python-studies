def insertion_sort(lista_a):
    index_tamanho = range(1, len(lista_a))
    for i in index_tamanho:
        valor_a_organizar = lista_a[i]

        while lista_a[i-1] > valor_a_organizar and i>0:
            lista_a[i], lista_a[i-1] = lista_a[i-1], lista_a[i]
            i = i -1

    return lista_a

print(insertion_sort([2, 4, 6, 5, 7, 8]))
