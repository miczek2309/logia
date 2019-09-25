def suma_wrzystkich_liczb(lista):
    n = 0
    u = 1
    for i in lista[:-1]:
        for z in lista[u:]:
            if i != z:
                n = n + (i + z)
        u = u + 1
    return n
print((suma_wrzystkich_liczb([2, 4, 1])))
           
           
           
           
       
    
