senhas = []
contador = 0
usuarios = int(input("Quantos usuários estão no sistema?\n"))
for i in range(usuarios):
    senhas.append(input("Digite a senha de um dos usuários restantes\n"))

for i in range(len(senhas)):

    for j in range (len(senhas)):
        if senhas[i] in senhas[j] and i != j:
            contador+= 1

print(contador)

