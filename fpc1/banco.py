t = int(input())
casos = [[]]
condicional = False

for i in range(t):
    if 1 > t or t > 1000:
        break
    n = int(input())
    if n < 1 or n > 1000:
        break

    f = []
    p = []
    casos += [[]]

    for j in range(n):
        entrada = list(map(str, input().split()))
        if len(entrada) > 1: 
            if int(entrada[1]) < 1 or int(entrada[1]) > 100:
                condicional = True
                break

        if entrada[0] == "f":
            f.append(entrada[1])
        elif entrada[0] == "p":
            p.append(entrada[1])
        elif entrada[0] == "I":
            if f and p:
                casos[i].append((f[0], p[0]))
            elif f and not p:
                casos[i].append((f[0],"0"))
            elif not f and p:
                casos[i].append(("0", p[0]))
            elif not f and not p:
                casos[i].append(("0","0"))
        elif f and entrada[0] == "A":
            f.pop(0)
        elif not f and entrada[0] == "A":
            p.pop(0)
        elif p and entrada[0] == "B":
            p.pop(0)
        elif not p and entrada[0] == "B":
            f.pop(0)
    if condicional:
        break

if casos[0]:
    for m in range(len(casos)-1):
        print("Caso "+ str(m+1) + ":" )
        for n in range(len(casos[m])):
            print(casos[m][n][0], casos[m][n][1])