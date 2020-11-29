"""

## 2. Pętle i struktury danych
### Zadanie 2.1 | Zagadka matematyczna

Program losuje dwie liczby z zakresu od 0 do 99 (patrz poniżej).
Podaje te dwie liczby i pyta jaka jest ich suma (nie podaje jej).
Użytkownik ma odgadnąć (no, policzyć w głowie) wynik.
Program pyta o wynik wielokrotnie, tak długo, aż użytkownik poda prawidłowy wynik.

"""
from random import randint

a = randint(0, 99)
b = randint(0, 99)
suma = a + b
while True:
    suma_uzytkownika = int(input(f'Wylosowane liczby to {a} oraz {b}. Jaka jest ich suma? '))
    if suma == suma_uzytkownika:
        print(f"Podales poprawna odpowiedz, suma {a} i {b} to: {suma_uzytkownika}")
        break
