def najmniejsza_ruznica(N):
    reka = 0
    u = 1
    e = 0
    t = 0
    for i in N[:len(N) - 1]:
        for x in N[u:]:
            e = i - x
            t = x - i
            if e < reka:
                reka = e
            elif t < reka:
                reka = t
        u = u + 1
    return reka
print(najmniejsza_ruznica([1, 1, 2, 3, 7]))
            
        
