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
liczba_rzedow = 1 #a1
r = 2
a1 = 1
szerokosc_choinki = a1 + (wysokosc_choinki - 1) * r #an
while liczba_rzedow <= wysokosc_choinki:
    liczba_znakow = a1 + (liczba_rzedow - 1) * r
    #liczba_spacji = wysokosc_choinki - liczba_znakow #krzywy worek sw Mikolaja (bez MIkolaja)
    liczba_spacji = wysokosc_choinki - liczba_rzedow
    znak = '*'
    spacja = ' '
    print(f'{spacja:2}' * liczba_spacji, end="")
    print(f'{znak:2}' * liczba_znakow, end="")
    liczba_rzedow += 1
    print(" ")
