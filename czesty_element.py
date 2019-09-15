def czesty_element(lista):
    n = 0
    reka = 0
    for i in lista:
        for x in lista:
            if i == x:            
                n = n + 1
            if n > reka:
                reka = n
        n = 0
    return reka
print(czesty_element([1, 4, 2, 4, 4, 5, 5, 5, 5]))
                    
