def ile(numer_miesaca, numer_dnia):
    liczba_dni = 0
    dzien = 0
    for m in range(1, numer_miesaca):
        if m % 2 == 0:
            liczba_dni = 15
            dzien = dzien + liczba_dni
        else:
            liczba_dni = 12 
            dzien = dzien + liczba_dni
    return numer_dnia - 1 + dzien
print("ile(1, 8) = ", ile(1, 8))
print("ile(10, 4) = ", ile(10, 4))
print("ile(20, 15) = ", ile(20, 15))
print("ile(1, 1) = ", ile(1, 1))
