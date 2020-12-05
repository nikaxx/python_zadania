"""
Mam listę liczb w zmiennej a.
chcemy w zmiennej b stworzyć listę zawierającą jedynie liczby większe od 50
b ma mieć zawartość: [400, 90, 100, 234 ... ] itd
"""

# TODO
a = [1, 3, 7, 20, 90, 100, 234, 3423, 4343]
b = []
for liczba in a:
    if liczba > 50:
        b.append(liczba)
print(b)