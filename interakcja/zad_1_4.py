"""
### Zadanie 1.4 | Opłata hotelowa (ok 1,5 godz.)

Potem napisz taki program: użytkownik podaje swój wiek i ile nocy spędzi w hotelu,
a program wylicza, ile trzeba zapłacić. Zasady są takie:

- nieletni (poniżej 18 roku życia) płacą 100 zł za noc
- dorośli (ci, którzy mają przynajmniej 18 lat ale mniej niż 65 lat) płacą:
	- 200 zł za noc, jeśli nocują jedną noc
	- 180 zł za noc, jeśli nocują przynajmniej dwie ale mniej niż pięć nocy
	- 150 zł za noc, jeśli nocują pięć lub więcej nocy
- emeryci (ci, którzy mają przynajmniej 65 lat), płacą jak dorośli, ale z 10% zniżki

Przykładowo: jeśli użytkownik ma 70 lat i spędzi w hotelu dziesięć nocy, zapłaci 150 zł za noc z 10% zniżki,
 czyli 150-15 zł za noc, czyli 135 zł za noc, czyli 1350 zł.
"""
wiek = int(input("Podaj swoj wiek: "))
ilosc_nocy = int(input("Ile nocy chcesz spedzic w hotelu: "))
cena_za_noc = 0
naleznosc = 0

if wiek < 18:
    cena_za_noc = 100
else:
    if ilosc_nocy == 1:
        cena_za_noc = 200
    elif 5 < ilosc_nocy <= 2:
        cena_za_noc = 180
    elif ilosc_nocy >= 5:
        cena_za_noc = 150

if wiek >= 65:
    cena_za_noc *= 0.9

naleznosc = cena_za_noc * ilosc_nocy

print(f'Nalezy zaplacic {naleznosc} PLN za {ilosc_nocy} nocy w hotelu dla goscia, ktory ma {wiek} lat.')
