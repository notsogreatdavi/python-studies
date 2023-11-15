somanumeros = 0
numeros = []
while True:
    qnumeros = int(input("Quantos números o seu chefe falou, contando com os zeros?\n"))
    if qnumeros >= 1 and qnumeros <= 100000:
        break

for i in range(qnumeros):
    while True:
        numero = int(input("Digite em ordem crescente os números ditos, linha por linha\n"))
        if  numero >= 0 and numero <= 100:
            break

    if numero != 0:
        numeros.append(numero)
    else:
        del numeros[-1]

for numero in numeros:
    somanumeros += numero

if somanumeros > 1000000:
    print("A soma passou do limite perdido")
    
print(somanumeros)
