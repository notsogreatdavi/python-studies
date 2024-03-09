def somar_lista(lista):
    soma = 0
    for i in lista:
        soma += i
    return soma

    
def encontrar_peca_perdida(n_pecas,lista_incompleta):   
    soma_lista_incompleta = somar_lista(lista_incompleta)

    soma_lista_completa = int((n_pecas * (n_pecas + 1)) / 2)
    peca_perdida = soma_lista_completa - soma_lista_incompleta
    print(peca_perdida)


def main():
    n_pecas = int(input())
    lista_incompleta = [int(i) for i in input().split()]
    encontrar_peca_perdida(n_pecas,lista_incompleta)

main()