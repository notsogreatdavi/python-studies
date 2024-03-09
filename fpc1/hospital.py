
qtd_pacientes = int(input())
lista_pacientes = []
for _ in range(qtd_pacientes):
    nome, plano, gravidade = input().split()
    lista_pacientes.append((nome, plano, gravidade))

def organizar_fila(pacientes):
    if len(pacientes) <= 1:
        return pacientes
    def trocar(pacientes, i, j):
        pacientes[i], pacientes[j] = pacientes[j], pacientes[i]
    def particionar(pacientes, low, high):
        pivot = pacientes[high]
        i = low
        for j in range(low, high):
            if prioridade(pacientes[j]) < prioridade(pivot):
                trocar(pacientes, i, j)
                i += 1
            elif prioridade(pacientes[j]) == prioridade(pivot) and pacientes[j][0] < pivot[0]:
                trocar(pacientes, i, j)
                i += 1
        trocar(pacientes, i, high)
        return i
    def quicksort(pacientes, low, high):
        if low < high:
            pi = particionar(pacientes, low, high)
            quicksort(pacientes, low, pi - 1)
            quicksort(pacientes, pi + 1, high)
    def prioridade(paciente):
        planos = {"premium": 5, "diamante": 4, "ouro": 3, "prata": 2, "bronze": 1, "resto": 0}
        return (
            -planos[paciente[1]],  
            -int(paciente[2]),  
            paciente[0] 
        )
    quicksort(pacientes, 0, len(pacientes) - 1)
    return pacientes

lista_ordenada = organizar_fila(lista_pacientes)

for paciente in lista_ordenada:
    print(paciente[0])