def silnia(N):
    s = 1
    for i in range(1, N+1):
        s = s*i
    return s
def silnia_2(N):
    if N == 1:
        return 1
    else:
        return silnia_2(N - 1) * N
print(silnia_2(4))
