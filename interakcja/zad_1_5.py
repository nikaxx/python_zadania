"""

### Zadanie 1.5 | Pole trójkąta (ok. 1 godz.)

Program, który odczytuje trzy liczby,
sprawdza czy liczby te mogą stanowić boki trójkąta (np. z 2, 2 i 5 nie da się ułożyć trójkąta, prawa?),
a jeśli mogą, oblicza pole powierzchni trójkąta o takich bokach.

Wykorzystaj trzeci wzór z [listy](https://www.matemaks.pl/wzory-na-pole-trojkata.html).

Tutaj użyj jednego z poznanych sposobów komunikacji z użytkownikiem. Pierwiastek kwadratowy to:

```
import math

x = math.sqrt(10)

"""
import math

a = float(input("Podaj pierwsza liczbe: "))
b = float(input("Podaj druga liczbe: "))
c = float(input("Podaj trzecia liczbe: "))
warunek = False
if a + b > c:
    if b + c > a:
        if a + c > b:
            warunek = True

p = (a + b + c) / 2 # polowa_obwodu_trojkata
pole_trojkata = math.sqrt(p * (p - a) * (p - b) * (p - c))
if warunek == True:
    print(f'Liczby: {a}, {b}, {c} moga stanowic boki trojkata.')
    print(f'Pole trojkata to: {pole_trojkata:.2f}.')
else:
    print(f'Liczby: {a}, {b}, {c} nie moga stanowic bokow trojkata.')
# Z drobiazgów - w 1.5 zamiast zagnieżdżać warunki możesz je połączyć używając and
#TODO