def ile_nie_parzystych_iloczynow(N):
    u = 1
    e = 0
    for i in N[:len(N) - 1]:
        for x in N[u:]:
            if i * x % 2 != 0:
                e = e + 1
        u = u + 1
    return e
print(ile_nie_parzystych_iloczynow([3, 5, 2, 7]))
            
    
