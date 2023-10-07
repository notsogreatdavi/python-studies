nome = input("Qual o seu nome?\n")
idade = input("Qual a sua idade?\n")

if nome != '' and idade != '':
    print("Seu nome é %s" % nome)
    print("Seu nome invertido é %s" % nome[::-1])
    if ' ' in nome:
        print("Seu nome contém espaços")
    else:
        print("Seu nome não contém espaços")
    print("Seu nome contém %s letras" % len(nome))
    print("A primeira letra do seu nome é %s" % nome[:1])
    print("A última letra do seu nome é %s" % nome[-1:])
else:
    print("Desculpe, você deixou campos vazios")