def F(n, contador):
    if n == 1:
        return contador + 1
    elif n % 2 == 0:
        return F(n // 2, contador + 1)
    else:
        return F(3 * n + 1, contador + 1)

def G(n):
   return F(n, 0)

qt_casos = int(input())
for i in range(qt_casos):
  A, B = map(int, input().split())
  chamadas = 0
  for n in range(A, B + 1):
      chamadas_g = G(n)
      if chamadas_g > chamadas:
          chamadas = chamadas_g
  print("Caso %d: %d" % (i+1, chamadas))