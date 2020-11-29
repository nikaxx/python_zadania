"""

## 1. Interakcja z użytkownikiem

### Zadanie 1.1 | Interakcja i proste obliczenia (ok. 2 godz.)

Napisz program, który prosi użytkownika (przez `input()`), żeby podał,
ile kosztuje kilo ziemniaków. Niech program policzy i wyświetli,
ile trzeba będzie zapłacić za pięć kilo ziemniaków.
"""
cena_jednostkowa = float(input("Podaj ile kosztuje kilo ziemnakow: "))
ilosc_kilogramow = 5
cena_koncowa = cena_jednostkowa * ilosc_kilogramow
towar = 'ziemniaki'
print(f'Za {ilosc_kilogramow} kg {towar} nalezy zaplacic {cena_koncowa:.2f} PLN')

