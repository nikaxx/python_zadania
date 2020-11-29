"""

### Zadanie 1.10 Położenie na planszy

Napisz program, który na podstawie pozycji gracza (x, y) na planszy w przedziale od 0 do 100
wyświetli jego przybliżone położenie (centrum, prawy górny róg, górna krawędź, ...)
lub informację o pozycji poza planszą. Przyjmij wartość 10 jako margines krawędzi.

Przykładowy komunikat programu:
Podaj pozycję gracza X: 95
Podaj pozycję gracza Y: 95
Gracz znajduje się w prawym górnym rogu.

Plansza poglądowa: https://drive.google.com/file/d/1Ek18pnoqiGiDcZJT6RBT1yufPUMaMJ7N/view?usp=sharing

"""
x = int(input("Podaj pozycje gracza X: "))
y = int(input("Podaj pozycje gracza Y: "))
pozycja_gracza = "Gracz znajduje sie "

if x < 0 or x > 100 or y < 0 or y > 100:
    pozycja_gracza += "poza plansza."
else:
    if 0 <= y <= 10:
        if 0 <= x <= 10:
            pozycja_gracza += "w lewym dolnym rogu."
        elif 10 < x < 90:
            pozycja_gracza += "w dolnym boku."
        else:
            pozycja_gracza += "w prawym dolnym rogu."
    elif 10 < y < 90:
        if 0 <= x <= 10:
            pozycja_gracza += "w lewym boku."
        elif 10 < x < 90:
            pozycja_gracza += "w srodku."
        else:
            pozycja_gracza += "w prawym boku."
    elif 90 <= y <= 100:
        if 0 <= x <= 10:
            pozycja_gracza += "w lewym gornym rogu."
        elif 10 < x < 90:
            pozycja_gracza += "w gornym boku."
        else:
            pozycja_gracza += "w prawym gornym rogu."

print(pozycja_gracza)