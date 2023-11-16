def cortar(tamanho_temp, tamanhos, fatias):
   cortes = 0
   for i in tamanhos:
       cortes += i // tamanho_temp
   return cortes >= fatias

def max_val(lista):
  valor_max = lista[0]
  for valor in lista:
      if valor > valor_max:
          valor_max = valor
  return valor_max

def bolo(fatias, bolos, tamanhos):
  inicio = 1
  fim = max_val(tamanhos)
  while fim - inicio > 1:
      meio = (inicio + fim) // 2
      if cortar(meio, tamanhos, fatias):
          inicio = meio
      else:
          fim = meio
  if cortar(fim, tamanhos, fatias):
      return fim
  else:
      return inicio

fatias = int(input())
bolos = int(input())
tamanhos = list(map(int, input().split()))
print(bolo(fatias, bolos, tamanhos))