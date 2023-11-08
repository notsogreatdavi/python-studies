def fibonacci(n):
    fib = [0] * (n+1)
    call = [0] * (n+1)
    fib[1] = 1
    call[1] = 0
    for i in range(2,n+1):
        fib[i] = fib[i-1] + fib[i-2]
        call[i] = call[i-1] + call[i-2] + 2
    return call[n], fib[n]

how_many_fib = int(input())
for i in range(how_many_fib):
    n = int(input())
    calls,result = fibonacci(n)
    print("fib(%d) = %d calls = %d" %(n,calls,result))
