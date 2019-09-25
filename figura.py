def figury(lista):
    u = 1
    e = 2
    for i in lista[:len(lista) - 3]:
        s = lista[u]
        f = lista[e]
        if i != s and i != f and s != f:
            return "TAK"
        u = u + 1
        e = e + 1
    return "NIE"
input()
b = [int(x) for x in input().split()]
print(figury(b))
    
