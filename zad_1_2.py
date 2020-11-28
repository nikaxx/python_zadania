"""

### Zadanie 1.2 | Buty do szewca (ok. 1 godz.)

Napisz taki program: użytkownik ma podać,
 w jaki dzień tygodnia oddał buty do szewca (poniedziałek to dzień 1, wtorek to dzień 2 itp.).
 Ma też podać, ile dni będzie trwała naprawa.

Program ma wypisać, w jaki dzień tygodnia buty będą gotowe do odbioru.
Jeśli tak będzie ci wygodniej, możesz założyć, że naprawa butów nigdy nie będzie trwała dłużej niż siedem dni.

"""

dzien_tygodnia = int(input("W jaki dzien oddales buty do szewca, podaj numer dnia: "))
ilosc_dni = int(input("Podaj ile dni ma trwac naprawa (max siedem dni): "))
reszta = (dzien_tygodnia + ilosc_dni) % 7

if 7 >= reszta > 0:
    dzien_odbioru = reszta
elif reszta == 0:
    dzien_odbioru = dzien_tygodnia

nazwa_dnia = None

if dzien_odbioru == 1:
    nazwa_dnia = 'poniedzialek'
elif dzien_odbioru == 2:
    nazwa_dnia = 'wtorek'
elif dzien_odbioru == 3:
    nazwa_dnia = 'sroda'
elif dzien_odbioru == 4:
    nazwa_dnia = 'czwartek'
elif dzien_odbioru == 5:
    nazwa_dnia = 'piatek'
elif dzien_odbioru == 6:
    nazwa_dnia = 'sobota'
elif dzien_odbioru == 7:
    nazwa_dnia = 'niedziela'

if nazwa_dnia is not None:
    print(f'Buty beda gotowe w {nazwa_dnia}.')