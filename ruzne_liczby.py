def rozne_liczby():
    lista_liczb_bez_powtarzania = []
    for i in range(100, 999):
        d = i
        a = d // 100
        d = d - 100 * a
        b = d // 10
        d = d - 10 * b
        c = d // 1
        d = i
        if a != b and a != c and b != c:
            lista_liczb_bez_powtarzania.append(d)
    return lista_liczb_bez_powtarzania

def rozne_liczby_2():
    lista_liczb_bez_powtarzania = []
    for s in range(1, 10):
        for d in range(0, 10):
            for j in range(0, 10):
                if s != d and d != j and s != j:
                    n = s * 100 + d * 10 + j
                    lista_liczb_bez_powtarzania.append(n)
    return lista_liczb_bez_powtarzania
print(len(rozne_liczby()))
        
                
        
        
        

