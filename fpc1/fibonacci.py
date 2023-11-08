def fibonacci(n, memo={}):
    if n <= 2:
        return 1
    elif n not in memo:
        memo[n] = fibonacci(n-1, memo) + fibonacci(n-2, memo)
    return memo[n]

howmany = int(input())
for i in range(howmany):
    x = int(input())
    print("fib(%d)  = %d" % (x, fibonacci(x)))
