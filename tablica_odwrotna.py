def tablica_odwrotna(N):
    tablica = []
    l = len(N)
    for i in range(l):
        l = l - 1
        d = N[l] 
        tablica.append(d)
    return tablica
print(tablica_odwrotna([2, 4, 5, 1]))
        
