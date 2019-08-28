
def Ile(lista):
    u = len(lista)
    if u == 0:
        print("lista nie ma cyfr")
    else:
        lista_bez_powtarzania = []
        l = lista[0]
        lista_bez_powtarzania.append(l)
        for i in lista[1:]:
            if i  not in lista_bez_powtarzania:
                lista_bez_powtarzania.append(i)
        e = len(lista_bez_powtarzania)
        return e
print(Ile([1, 5, 5, 2, 1]))


