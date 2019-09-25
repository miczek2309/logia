
def ile_zer(N):
    a = 0
    while N > 0:
        cyfra = N % 10
        if cyfra == 0:
            a = a + 1
        N = N // 10
    return a

def ile_zer_2(N):
    return str(N).count('0')

print(ile_zer_2(1001230))

