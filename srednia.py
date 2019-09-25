def srednia(lista, a, b):
    t = lista[0]
    for i in lista[1:]:
        t = t + i
    print(t)
    return t // n
 n int(input())
l = [int(x) for x in input().split()]
print(l)
c, d = [int(u) for u in input().split()]
print(srednia(l, c, d))
