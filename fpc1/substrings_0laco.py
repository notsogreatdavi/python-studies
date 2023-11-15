def exibir_subs(palavra, comprimento=1, inicio=0):
    comprimento_palavra = len(palavra)
    if comprimento > comprimento_palavra:
        return
    fim = inicio + comprimento
    print(palavra[inicio:fim])
    if inicio + comprimento == comprimento_palavra:
        substrings_recursive(palavra, comprimento + 1, 0)
    else:
        substrings_recursive(palavra, comprimento, inicio + 1)

exibir_subs(input())
