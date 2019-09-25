def szlaczek(N):
    if N % 2 == 0:
        I = N
        for i in range(I // 2):
            print("+", end="")
            print("-", end="")
    else:
        I = N - 1
        for i in range(I // 2):
            print("+", end="")
            print("-", end="")
        print("+")
    print()

def slaczek_taty(N):
    s = ""
    for i in range(N):
        if i % 2 == 1:
            s = s + "-"
        else:
            s = s + "+"
    print(s)
    
         
slaczek_taty(5)
