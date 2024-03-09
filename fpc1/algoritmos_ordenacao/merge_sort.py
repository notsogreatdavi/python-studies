def merge(A, p, q, r):
    L = A[p : q + 1]
    L += [float("inf")]
    R = A[q + 1 : r + 1]
    R += [float("inf")]
    i = j = 0
    for k in range(p, r + 1):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1

def merge_sort(A, p, r):
    if p < r:
        q = int((p + r) / 2)
        merge_sort(A, p, q)
        merge_sort(A, q + 1, r)
        merge(A, p, q, r)

A = list(range(100, 0, -1))
merge_sort(A, 0, len(A) - 1)
print(A)
