"""
Mam listę liczb w zmiennej a.
chcemy w zmiennej b stworzyć listę zawierającą pięciokrotności każdej z liczb, czyli np.
b ma mieć zawartość: [5, 15, 35, 100 ... ] itd
"""

a = [1, 3, 7, 20, 90, 100, 234, 3423, 4343]
b = []
for liczba in a:
    b.append(liczba * 5)
print(f"Lista zawierajaca pieciokrotnosc to: {b}")