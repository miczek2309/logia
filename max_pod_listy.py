def max_listy_list(lista):
    for i in lista:
        reka = 0
        for x in i:
            if x > reka:
                reka = x
        print(reka,end=" ")
max_listy_list([[2, 5], [8, 10], [0, 1]])
