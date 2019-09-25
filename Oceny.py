def oceny(lista):
    u = 1
    ile = 0
    while u < 7:
        for i in lista:
            if u == i:
                ile = ile + 1
        print(ile,end=" ")
        ile = 0
        u = u + 1
input()
lista_1 = [int(x) for x in input().split()]
oceny(lista_1)
