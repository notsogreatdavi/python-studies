def encontrar_pasto(T, i, j, n, m):
    if i < 0 or i >= n or j < 0 or j >= m:
        return 0, 0
    if T[i][j] == '#':
        return 0, 0
    ovelhas, lobos = 0, 0
    if T[i][j] == 'k':
        ovelhas = 1
    elif T[i][j] == 'v':
        lobos = 1
    T[i][j] = '#'
    for x, y in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        o, l = encontrar_pasto(T, i + x, j + y, n, m)
        ovelhas += o
        lobos += l
    return ovelhas, lobos

def contar_sobreviventes(T):
    n, m = len(T), len(T[0])
    total_ovelhas, total_lobos = 0, 0
    for i in range(n):
        for j in range(m):
            if T[i][j] in ('k', 'v'):
                ovelhas, lobos = encontrar_pasto(T, i, j, n, m)
                if ovelhas > lobos:
                    total_ovelhas += ovelhas
                else:
                    total_lobos += lobos
    return total_ovelhas, total_lobos

N, M = map(int, input().split())
T = []
for _ in range(N):
    linha = list(input())
    T.append(linha)

ovelhas_sobreviventes, lobos_sobreviventes = contar_sobreviventes(T)


print(ovelhas_sobreviventes, lobos_sobreviventes)