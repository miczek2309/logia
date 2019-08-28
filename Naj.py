
def NAJ(lista):
    parzyste_liczby = []
    for n in lista:
        if n % 2 == 0:
            parzyste_liczby.append(n)
    jan = len(parzyste_liczby)
    if jan > 1:
        if parzyste_liczby[0] >= parzyste_liczby[1]:
            reka = parzyste_liczby[0]
        else:
            reka = parzyste_liczby[1]      
        for a in parzyste_liczby:
            if reka < a:
                reka = a                    
    else:          
        reka = parzyste_liczby[0]
    return reka
    
print(NAJ([9000, 202, 300, 201, 1000]))
