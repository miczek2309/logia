def czy_takie_same(N, A):
    s = sorted(N)
    u = sorted(A)
    if s == u:
        return True
    else:
        return False
print(czy_takie_same([2, 5, 3, 3], [3, 5, 2, 3]))
    
