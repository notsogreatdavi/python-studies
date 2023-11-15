def substrings(s):
    n = len(s)
    for length in range(1, n + 1):
        for start in range(n - length + 1):
            end = start + length
            print(s[start:end])

substrings(input())