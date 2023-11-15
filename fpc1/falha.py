senhas = []
contador = 0
while True: 
    usuarios = int(input("Quantos usuários estão no sistema?\n"))
    if usuarios >= 1 and usuarios <= 2000:
        break
    
for i in range(usuarios):
    while True:
        senha = (input("Digite a senha de um dos usuários restantes\n"))
        if len(senha) <= 10 and len(senha) >= 1 and senha.islower() and senha.isascii:
            senhas.append(senha)
            break

for i in range(len(senhas)):
    for j in range (len(senhas)):
        if senhas[i] in senhas[j] and i != j:
            contador+= 1

print(contador)