
def najwieksza_suma(lista):
    n = 0
    reka = 0
    for i in lista[1:]:
        for x in lista:
            if x != i:
                n = x + i
            if reka < n:
                reka = n
    return reka

print(najwieksza_suma([2, 5, 8, 10, 5]))

            
        
        
