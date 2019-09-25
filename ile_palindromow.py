def ile_palindrom(lista):
    ile = 0
    for lancuch in lista:
        palindrom = []
        palindrom2 = []
        for i in lancuch:
           palindrom.append(i)
        l = len(palindrom)
        l = l - 1
        while l >=  0:
            p = palindrom[l]
            palindrom2.append(p)
            l = l - 1
        if palindrom2 == palindrom:
            ile = ile + 1
    print(ile)
ile_palindrom(['kajak', 'ala', 'elo', 'ulu'])
        

        
