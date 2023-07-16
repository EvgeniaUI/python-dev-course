def nod(n, k):
    num_1 = min(n, k)
    num_2 = max(n, k)
    nod = num_1
    if num_1 == num_2 or num_2 % num_1 == 0:
        return num_1
    nod -= 1
    while nod > 0:
        if num_1 % nod == 0 and num_2 % nod == 0:
            return nod
        nod -= 1

n, k = map(int, input().split())
print(nod(n, k))
