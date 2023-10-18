somanumeros = 0
numeros = []
qnumeros = int(input("Quantos números o seu chefe falou, contando com os zeros?\n"))

for i in range(qnumeros):
    numero = int(input("Digite em ordem crescente os números ditos, linha por linha\n"))
    if numero != 0:
        numeros.append(numero)
    else:
        del numeros[-1]
        
for numero in numeros:
    somanumeros += numero
print(somanumeros)
