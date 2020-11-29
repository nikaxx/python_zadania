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

"""
# liczba_rzedow = int(input("Podaj liczbe rzedow choinki: "))
liczba_rzedow = 5

while liczba_rzedow > 0:
    liczba_znakow = 5
    while liczba_znakow > 0:

        print("*", end="")
        liczba_znakow -= 1
    print(" ")
    liczba_rzedow -= 1
