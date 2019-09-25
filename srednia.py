def srednia(lista, a, b):
    suma = 0
    for i in range(a - 1, b):
        suma = suma + lista[i]
    return suma // (b - a + 1)
input()
l = [int(x) for x in input().split()]
c, d = [int(y) for y in input().split()]
print(srednia(l, c, d))
