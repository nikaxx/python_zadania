"""
### Zadanie 2.6 Zliczanie znaków w napisie

Napisz program zliczający liczbę znaków w podanym przez użytkownika napisie
pomiędzy nawiasami <>. Nawiasy mogą wystąpić tylko raz.
Ala ma <kota>, a kot ma Alę
4


1. Sprawdzam liczbę < i > - powinno ich być po jednym,
      jeżeli liczba tych nawiasów jest inna, to kończę program
2. W pętli sprawdzam czy:
      - mam zliczac
      - mam przestać zliczać
      - czy zliczanie jest włączone i wtedy zliczam
"""
warunek = False
napis = input("Podaj napis:")
#napis = "Ala ma <kota>, a kot ma Alę"
ilosc_nawiasow_otwierajacych = napis.count("<")
ilosc_nawiasow_zamykajacych = napis.count(">")
if ilosc_nawiasow_otwierajacych == 1 & ilosc_nawiasow_zamykajacych == 1:
    warunek = True
print(warunek)
zliczac = False
if warunek:
    napis_wewnetrzny = ""
    for znak in napis:
        if znak == ">":
            zliczac = False
        if zliczac:
            napis_wewnetrzny += znak
        if znak == "<":
            zliczac = True

    print(len(napis_wewnetrzny))


