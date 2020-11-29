"""

### Zadanie 1.7 | Liczenie cen (ok. 0,5 godz.)
Przy pomocy `input()` zapytaj użytkownika co chce kupić,
jaką ilość towaru chce kupić i jaka jest jego cena.
Wyświetl odpowiedni komunikat.
Przykład:
Co chcesz kupić? - ziemniaki
Podaj cenę towaru - 5
Podaj ilość towaru - 10
Za ziemniaki, który chcesz kupić, zapłacisz 50 zł
"""
towar = input("Co chcesz kupic? ")
ilosc_towaru = float(input(f"Ile kilogramow {towar} chcesz kupic? "))
cena_towaru =  float(input(f"Ile kosztuje {towar}: "))
naleznosc = ilosc_towaru * cena_towaru

print(f'Za {towar}, ktory chcesz kupic w ilosci {ilosc_towaru} kg zaplacisz {naleznosc:.2f} PLN')