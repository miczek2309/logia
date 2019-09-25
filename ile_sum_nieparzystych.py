def ile_sum_nieparzystych(lista):
    lista_sum_nieparzystych = []
    u = 1
    for i in lista[:len(lista) - 1]:
        for z in lista[u:]:
            suma = i + z
            if suma % 2 == 1:
                lista_sum_nieparzystych.append(suma)
        u = u + 1
    l = len(lista_sum_nieparzystych)
    return l
print(ile_sum_nieparzystych([2, 4, 5, 3]))
        
