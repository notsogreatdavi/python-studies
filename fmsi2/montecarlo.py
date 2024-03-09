import numpy as np

num_experimentos = 1000
n = 100000

#cria um array para armazenar as áreas estimadas de pi para cada experimento
areas_experimentos = np.zeros(num_experimentos)

for experimento in range(num_experimentos):
    
    pontos = np.random.uniform(-1, 1, size=(n, 2))

#faz o calculo da quantidade de pontos dentro do círculo
    nc = np.sum(pontos[:, 0]*2 + pontos[:, 1]*2 <= 1)

    area_pi = 4 * nc / n
    areas_experimentos[experimento] = area_pi

media_areas = round(np.mean(areas_experimentos), 10)
print(f"Média das áreas estimadas: {media_areas}")