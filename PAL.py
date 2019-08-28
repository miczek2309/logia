
def PAL(lancuch):
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
        print("slowo jest palindromem")
    elif palindrom2 != palindrom:
        print("slowo nie jest palindromem")
    
        
PAL("kajak")
