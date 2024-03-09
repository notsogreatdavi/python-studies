def calcular_distancia(A, B):
    m, n = len(A), len(B)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0:
                dp[i][j] = j
            elif j == 0:
                dp[i][j] = i
            elif A[i - 1] == B[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j],
                                  dp[i][j - 1],
                                  dp[i - 1][j - 1])

    return dp[m][n]

def buscar_palavras(dicionario, palavra):
    palavras_ref = []

    for palavra_dict in dicionario:
        distancia = calcular_distancia(palavra, palavra_dict)
        if distancia <= 2:
            palavras_ref.append(palavra_dict)

    return palavras_ref

def main():
    N, M = map(int, input().split())
    dicionario = [input().strip() for _ in range(N)]
    palavras_user = [input().strip() for _ in range(M)]

    for palavra in palavras_user:
        palavras_ref = buscar_palavras(dicionario, palavra)
        if palavras_ref:
            print(" ".join(palavras_ref))
        else:
            print()

if __name__ == "__main__":
    main()