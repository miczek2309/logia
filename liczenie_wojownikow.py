liczba_budynkuw = 3
liczba_wojownikow_ninja_na_budynku = 25
liczba_tuneli = 2
liczba_samuraji_w_tunelach = 40
liczba_wojownikow = (liczba_budynkuw * liczba_wojownikow_ninja_na_budynku) + (liczba_tuneli * liczba_samuraji_w_tunelach)
wynik = '%s wojownikow stanie do walki'
print(wynik % liczba_wojownikow)
