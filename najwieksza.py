def najwieksza(lista):
    a = lista[0]
    b = lista[1]
    c = lista[2]
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c
print(najwieksza([1, 2, 3]))
    
