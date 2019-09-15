def potegi(N):
    i = 1
    while i <= N:
        print(i, end="")
        i = i * 2
        if i <= N:
            print(", ", end="")
potegi(512) 
    
