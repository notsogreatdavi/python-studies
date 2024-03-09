vertical = int(input())
horizontal = list(map(int, input().split()))

def contar_cruzamentos(n, ordem_horizontal):
    qtd_cruzamentos = 0
    for i in range(n - 1):
        for j in range(i + 1, n):
            if horizontal[i] > horizontal[j]:
                qtd_cruzamentos += 1
    return qtd_cruzamentos


cruzamentos = contar_cruzamentos(vertical, horizontal)
print(cruzamentos)