def przeplatana_tablica(N, T):
    tablica = []
    l = len(N)
    for d in N:
        tablica.append(d)
        for i in T[:1]:
            tablica.append(i)
            del T[0]
    return tablica
print(przeplatana_tablica([4, 2, 5], [8, 3, 2]))
        
    
