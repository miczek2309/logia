def ile_samoglosek(napis):
    n = 0
    lista_samoglosek = ['a', 'A', 'e', 'E', 'y', 'Y', 'o', 'O', 'i', 'I']
    for i in napis:
            if i in lista_samoglosek:
                n = n + 1
    return n
print(ile_samoglosek("AaBccIOOOEyecie pecie"))
