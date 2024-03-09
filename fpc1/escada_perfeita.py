qtd_pilhas = int(input())
pilhas = [int(i) for i in input().split()]

base = (qtd_pilhas*(qtd_pilhas + 1))/2
total_pedras = int()
for pilha in pilhas:
    total_pedras += pilha

sobra = int(total_pedras - base)
inicio = int(sobra / qtd_pilhas)

if sobra % qtd_pilhas != 0:  
    print('-1')
else:
    movimentos = 0
    for i, coluna in enumerate(pilhas):
        if coluna > (inicio + i + 1):
            movimentos += coluna - (inicio + i + 1)
    print(movimentos)