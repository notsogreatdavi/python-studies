def fatorial(n):
    if n <= 1:
        return n
    return n * fatorial(n-1)


def main():
    numero = int(input("Você deseja o fatorial de qual número? "))
    print("O fatorial de {} é {}".format(numero, fatorial(numero)))


if __name__ == '__main__':
    main()