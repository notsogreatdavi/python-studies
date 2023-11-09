def Mdc(figurinhas1, figurinhas2):
   while figurinhas2 != 0:
       figurinhas1, figurinhas2 = figurinhas2, figurinhas1 % figurinhas2
   return figurinhas1

casos = int(input())
for i in range(casos):
   figurinhas1, figurinhas2 = map(int, input().split())
   print(Mdc(figurinhas1, figurinhas2))
