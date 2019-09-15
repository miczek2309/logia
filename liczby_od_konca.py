
def liczby_od_konica(N):
    lista_od_konca = []
    while N >= 1:
        lista_od_konca.append(N)
        N = N - 1  
    return lista_od_konca

print(liczby_od_konica(20))
