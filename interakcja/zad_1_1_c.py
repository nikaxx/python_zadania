"""

## 1. Interakcja z użytkownikiem

### Zadanie 1.1 | Interakcja i proste obliczenia (ok. 2 godz.)

Potem napisz program, który prosi użytkownika (przez `input()`),
żeby podał, ile kosztuje kilo ziemniaków, ile kilo ziemniaków chce kupić,
ile kosztuje kilo bananów i ile kilo bananów chce kupić.
Niech program policzy i wyświetli, ile trzeba będzie zapłacić za te ziemniaki i banany razem.
I niech program sprawdzi i powie, za co trzeba będzie zapłacić więcej - za banany czy za ziemniaki.

"""
towar1 = 'ziemniaki'
cena_jednostkowa_towar1 = float(input("Podaj ile kosztuje kilo ziemnakow: "))
ilosc_kilogramow_towar1 = float(input("Podaj ile kilogramow chcesz kupic: "))
cena_koncowa_towar1 = cena_jednostkowa_towar1 * ilosc_kilogramow_towar1

towar2 = 'banany'
cena_jednostkowa_towar2 = float(input("Podaj ile kosztuje kilo bananow: "))
ilosc_kilogramow_towar2 = float(input("Podaj ile kilogramow chcesz kupic: "))
cena_koncowa_towar2 = cena_jednostkowa_towar2 * ilosc_kilogramow_towar2

naleznosc = cena_koncowa_towar1 + cena_koncowa_towar2


print(f'Za {ilosc_kilogramow_towar1} kg {towar1} '
      f'oraz za {ilosc_kilogramow_towar2} kg {towar2} '
      f'nalezy zaplacic {naleznosc:.2f} PLN')

if cena_koncowa_towar1 > cena_koncowa_towar2:
    print(f'Trzeba zaplacic wiecej za {towar1}.')
elif cena_koncowa_towar1 < cena_koncowa_towar2:
    print(f'Trzeba zaplacic wiecej za {towar2}.')
else:
    print(f'Za {towar1} oraz {towar2} trzeba zaplacic tyle samo!')
