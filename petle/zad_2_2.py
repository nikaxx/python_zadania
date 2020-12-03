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
kursor = - wysokosc_choinki + 1
max_znakow = a1 + (wysokosc_choinki - 1) * r #an
temp3 = wysokosc_choinki
while liczba_rzedow <= wysokosc_choinki:
    liczba_znakow = a1 + (liczba_rzedow - 1) * r
    temp = kursor
    temp2 = max_znakow
    while temp2 > 0:
        znak = '*'
        spacja = ' '
        if temp < 0:
            print(f'{spacja:<2}', end="")
        elif temp == 0:
            print(f'{znak:<2}' * liczba_znakow, end="")
            temp2 -= liczba_znakow + 1
            temp = 1
        temp2 -= 1
        temp += 1
    liczba_rzedow += 1
    kursor += 1
    print(" ")