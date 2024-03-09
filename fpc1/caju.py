def cajus(soma, memo, i, j, M, N):
    if i + M > len(soma) or j + N > len(soma[0]):
        return 0
    
    if memo[i][j] != -1:
        return memo[i][j]
    
    total = soma[i + M - 1][j + N - 1]
    if i > 0:
        total -= soma[i - 1][j + N - 1]
    if j > 0:
        total -= soma[i + M - 1][j - 1]
    if i > 0 and j > 0:
        total += soma[i - 1][j - 1]
    
    memo[i][j] = max(total, cajus(soma, memo, i + 1, j, M, N), cajus(soma, memo, i, j + 1, M, N))
    return memo[i][j]

def calcular_colheita():
    L, C, M, N = map(int, input().split())
    
    fazenda = [list(map(int, input().split())) for _ in range(L)]
    
    soma = [[0] * C for _ in range(L)]
    for i in range(L):
        for j in range(C):
            soma[i][j] = fazenda[i][j]
            if i > 0:
                soma[i][j] += soma[i - 1][j]
            if j > 0:
                soma[i][j] += soma[i][j - 1]
            if i > 0 and j > 0:
                soma[i][j] -= soma[i - 1][j - 1]
    
    memo = [[-1] * C for _ in range(L)]
    
    result = cajus(soma, memo, 0, 0, M, N)
    
    print(result)

if __name__ == "__main__":
    calcular_colheita()
    