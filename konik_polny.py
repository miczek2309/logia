def konik_polny(x, y):
    dlugosc = 0
    ile = 0
    while dlugosc < y and x > 1:
        dlugosc = dlugosc + x
        x = x // 2
        ile = ile + 1
    if dlugosc >= y:
        return ile
    else:
        i = y - dlugosc
        ile = ile + i
    return ile
a, b = [int(z) for z in input().split()]
print(konik_polny(b, a))    
