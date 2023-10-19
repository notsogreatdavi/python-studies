while True:
    qregistros = int(input("Qual o número de registros?\n"))
    if qregistros >= 1 and qregistros <= 20:
        break

registros = []
recebidos = []
usuarios_tempos = {}
tempo_total = 0

for i in range(qregistros):
   registro =  registros.append(input("Me diga qual o registro que deseja informar\n"))

for i in range(len(registros)):
    if registros[i][:1] == 'R':
        recebidos.append(registros[i][2:])
        foi_tempo = False
        respondida = False
    if registros[i][:1] == 'T':
        tempo_total += int(registros[i][2:])
        foi_tempo = True
    if registros[i][:1] == 'E':
        if foi_tempo == True:
            tempo_total += 1
        if registros[i][2:] in recebidos:
            respondida = True
            usuarios_tempos[registros[i][2:]] = tempo_total
        elif respondida == False:
            usuarios_tempos[registros[i][2:]] = -1
        foi_tempo = False

for usuario, tempo in usuarios_tempos.items():
    print(usuario, tempo)




