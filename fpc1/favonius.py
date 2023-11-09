def favonius(pessoas, salto):
   sobrevivente = 0
   for i in range(2, pessoas+1):
       sobrevivente = (sobrevivente + salto) % i
   return sobrevivente + 1

casos = int(input())

for i in range(casos):
    pessoas, salto = map(int, input().split())
    print("Case %d: %d" % (i+1, favonius(pessoas, salto)))