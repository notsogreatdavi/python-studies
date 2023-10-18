while True:
    numero = int(input("Qual o número que você deseja contar? Lembre-se que ele deve ser maior ou igual a zero e menor ou igual a dez\n"))
    if (numero > 0) or (numero < 10):
        break

if numero <= 5:
    print("I" * numero);

if numero > 5:
    print("")