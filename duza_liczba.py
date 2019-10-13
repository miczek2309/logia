def duza_liczba(lista1):
    zbior = set(lista1)
    lista = sorted(list(zbior),reverse=True)
    s = 0
    for i in lista:
        s = s * 10 + i
    return s
lista = [int(x) for x in input().split()]
print(duza_liczba(lista))
                
            
    
        
        
