def wagony(lista, a, b):
    reka = -100000
    for i in lista[a-1:b]:
        if i % 2 == 1 and i > reka:
            reka = i
    return reka
input()
lista = [int(x) for x in input().split()]
c, d = [int(y) for y in input().split()]
print(wagony(lista, c, d))
 
