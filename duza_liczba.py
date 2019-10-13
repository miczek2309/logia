def duza_liczba(lista1):
    lista = []
    for x in lista1:
        if x not in lista:
            lista.append(x)
    lista = sorted(lista, reverse=True)
    s = 0
    for i in lista:
        s = s * 10 + i
    return s
lista = [int(x) for x in input().split()]
print(duza_liczba(lista))
                
            
    
        
        
