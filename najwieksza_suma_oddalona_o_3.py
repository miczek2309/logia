def najwieksza_suma_oddalona_o_3(N):
    u = 3
    reka = 0
    for i in N:
        for x in N[u:]:
            if i + x > reka:
                reka = i + x
        u = u + 1
    return reka
print(najwieksza_suma_oddalona_o_3([1, 2, 3, 5, 10, 2, 20, 22]))
