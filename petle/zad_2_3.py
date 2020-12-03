"""
### Zadanie 2.3
Napisz program, który odczytuje od użytkownika wiele liczb.
Program powinien wyliczyć i na końcu wypisać następujące statystyki:
- liczba podanych liczb (ile sztuk),
- suma,
- średnia,
- minimum
- maksimum
NIE używaj funkcji wbudowanych!
"""
liczby = []
ilosc_liczb = 0
suma_liczb = 0
minimum = None
maximum = None
while True:
    dane = input("Podaj liczbe lub napisz 'Koniec': ")
    if 'koniec' != dane.lower():
        liczba = int(dane)
        liczby.append(liczba)
        ilosc_liczb += 1
        suma_liczb += liczba
        if maximum is None or liczba > maximum:
            maximum = liczba
        if minimum is None or liczba < minimum:
            minimum = liczba
    else:
        break
print(f'Podales {ilosc_liczb} liczby.')
print(f'Suma podanych liczb wynosi: {suma_liczb}.')
print(f'Najmniejsza liczba wynosi: {minimum}.')
print(f'Najwieksza liczba wynosi: {maximum}.')


