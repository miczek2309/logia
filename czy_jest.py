def czy_jest(lista):
    for i in lista:
        if -i in lista:
            return True
    return False
lis = [int(x) for x in input().split()]
print(czy_jest(lis))
