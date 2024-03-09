def parent(i):
    return int(i/2)

def left_child(i):
    return 2*i + 1

def right_child(i):
    return 2*i + 2

def max_heapify(lista, indice, tamanho_heap):
    l = left_child(indice)
    r = right_child(indice)

    if l <= tamanho_heap and lista[l] > lista[indice]:
        maior = l
    else:
        maior = indice
    if r <= tamanho_heap and lista[r] > lista[maior]:
        maior = r
    if maior != indice:
        lista[indice], lista[maior] = lista[maior], lista[indice]
        max_heapify(lista, maior, tamanho_heap -1)

def build_max_heap(lista, tamanho_heap):
    tamanho_heap = len(lista)
    for indice in range(int(len(lista)/2), 0, -1):
        max_heapify(lista, indice, tamanho_heap)

def heapsort(lista, tamanho_heap):
    build_max_heap(lista, tamanho_heap)

    for indice in range(int(len(lista), 1, -1)):
        lista[1], lista[indice] = lista[indice], lista[1]
        tamanho_heap = tamanho_heap - 1
        max_heapify(lista, 1, tamanho_heap)
    return lista

lista = [16, 4, 10, 14, 7, 9, 3, 2, 8, 1]
lista_ordenada = heapsort(lista, len(lista))