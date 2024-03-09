movimento = {'N': ['O', 'L'], 'L': ['N', 'S'], 'S': ['L', 'O'], 'O': ['S', 'N']}
while True:
    linhas, colunas, qtd_instrucao = [int(i) for i in input().split()]
    if linhas == 0 and colunas == 0 and qtd_instrucao == 0:
        break
    var_auxiliar = 0
    posicao_linha = None
    posicao_coluna = None
    direcao = ''
    orientacao = None
    arena = []
    direcoes = ['N', 'S', 'O', 'L']
    for l in range(0, linhas):
        linha = input()
        if var_auxiliar == 0 and any(direc in linha for direc in direcoes):
            posicao_coluna = [linha.find(direc) for direc in direcoes]
            posicao_linha = l
            for num in range(0, len(posicao_coluna)):
                if posicao_coluna[num] != -1:
                    orientacao = direcoes[num]
                    posicao_coluna = posicao_coluna[num]
                    break
            var_auxiliar = 1
        arena.append(linha)
    instrucoes = input()
    pontuacao = 0
    for letra in instrucoes:
        if letra == 'D':
            orientacao = movimento[orientacao][1]
        elif letra == 'E':
            orientacao = movimento[orientacao][0]
        else:
            if orientacao == 'N' and posicao_linha > 0:
                if arena[posicao_linha - 1][posicao_coluna] == '#':
                    pass
                else:
                    posicao_linha -= 1
            elif orientacao == 'L' and posicao_coluna < colunas - 1:
                if arena[posicao_linha][posicao_coluna + 1] == '#':
                    pass
                else:
                    posicao_coluna += 1
            elif orientacao == 'S' and posicao_linha < linhas - 1:
                if arena[posicao_linha + 1][posicao_coluna] == '#':
                    pass
                else:
                    posicao_linha += 1
            elif orientacao == 'O' and posicao_coluna > 0:
                if arena[posicao_linha][posicao_coluna - 1] == '#':
                    pass
                else:
                    posicao_coluna -= 1
            if arena[posicao_linha][posicao_coluna] == '*':
                pontuacao += 1
                i = posicao_coluna
                arena[posicao_linha] = arena[posicao_linha][0:i] + '.' + arena[posicao_linha][i + 1:]
    print("\n", pontuacao)