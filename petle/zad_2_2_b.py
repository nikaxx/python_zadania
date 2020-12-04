"""

### Zadanie 2.2 | Choinka

Napisz program, który wczytuje liczbę całkowitą,
a następnie na konsolę wypisuje w tylu liniach "choinkę" ze znaków `*`.
Np. dla parametru 3 powinno się wypisać:

```
    *
  * * *
* * * * *
```
r = 2
a1 = 1
an = a1 + (n − 1)r
"""
wysokosc_choinki = int(input("Podaj wysokosc choinki: "))
szerokosc_choinki = 1 + (wysokosc_choinki - 1) * 2
znak = '*'
spacja = ' '
for wiersz in range(0, wysokosc_choinki):
    for kolumna in range(0, szerokosc_choinki):
        liczba = kolumna - wiersz
        if liczba == 0:
            print(f'{liczba:2}', end=' ')
        else:
            print(f'{liczba:2}', end=' ')
    print()
