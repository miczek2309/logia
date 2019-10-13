def taka_sama(lista1):
    reka = -100000
    suma = 0
    for u in range(len(lista1)):
        poczotek = lista1[u]
        for i in lista1:
            if i == poczotek:
                suma = suma * 10 + i
        if suma > reka:
            reka = suma
        suma = 0
    return reka
lista = [int(x) for x  in input().split()]
print(taka_sama(lista))
        
