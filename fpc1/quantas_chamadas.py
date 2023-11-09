def chamadas(n):
   call = [0] * (n+1)
   call[0] = 0
   for i in range(2, n+1):
       call[i] = call[i-1] + call[i-2] + 2
   return call[n]

counter = 0
while True:
   n, b = map(int, input().split())
   if n == 0 and b == 0:
       break
   counter += 1
   calls = chamadas(n)
   last_digit = (calls+1) % b
   print("Case %d : %d %d %d" %(counter,n,b,last_digit))