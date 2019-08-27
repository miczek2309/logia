import sys
def waga_na_ksiezycu():
    print("Prosze podaj swojo aktualno wage na planecie ziemia")
    waga = int(sys.stdin.readline())
    print("Prosze podaj, o ile Twoja waga rosnie kazdego roku")
    przyrost = float(sys.stdin.readline())
    print("Prosze podaj liczbe lat")
    okres = int(sys.stdin.readline())
    waga_aktualna = waga
    okres = okres + 1
    for rok in range(okres):
        waga_ksiezycowa = waga_aktualna * 0.165
        print(rok, waga_aktualna, waga_ksiezycowa)
        waga_aktualna = waga_aktualna + przyrost
waga_na_ksiezycu()
    
