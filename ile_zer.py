
def ile_zer(A):
    e = 10
    w = 0
    lista = []
    while A // e > 0:
        w = A // e
        e = e * 10
        lista.append(w)
        A = A // e
    return lista
print(ile_zer(100))

