"""
Mam listę liczb w zmiennej a.
chcemy w zmiennej b stworzyć listę zawierającą ciągi tekstowe postaci "xxxx"
w których liczba x-ów odpowiada liczbie z listy a.
Ale:
- zostawiamy tylko liczby parzyste
- jesli liczba jest większa niż 10, to piszemy tylko 10 x-ów (skracamy)

Czyli np.
a = [ 87, 93, 4, 13, 14, 8, 7, 3, 2, 100, 80, 81 ]
ma dać w rezultacie:
                         4      14 -> 10      8           2     100 -> 10     80 -> 10
listę b o zawartości: [ "xxxx", "xxxxxxxxxx", "xxxxxxxx", "xx", "xxxxxxxxxx", "xxxxxxxxxx" ]
"""
a = [ 87, 93, 4, 13, 14, 8, 7, 3, 2, 100, 80, 81 ]
b = []
for liczba in a:
    temp = ''
    if liczba % 2 == 0:
        if liczba > 10:
            liczba = 10
        temp = 'x' * liczba
        b.append(temp)
print(b)
# [x for x in lista]
#x for x in a if x > 50
c = [min(x, 10) * 'x' for x in a if x % 2 == 0]
print(c)