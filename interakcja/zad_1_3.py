"""
### Zadanie 1.3 | Współczynnik BMI (ok. 2 godz.)

Napisz program, który dla podanych liczb: wzrostu w cm i masy ciała w kg obliczą i wypisze współczynnik BMI,
 oraz podsumowanie informujące o stanie/zaleceniach.
 (Informacje o BMI: wzór, interpretację wyników, proszę znaleźć samodzielnie).
"""
wzrost = float(input("Podaj wzrost w centymetrach: "))
waga = float(input("Podaj wage w kilogramach: "))
bmi = waga / (wzrost / 100) ** 2
print(f'Twoje BMI to: {bmi:.1f}')
if bmi < 18.5:
    print("Masz niedowage!")
elif bmi < 25:
    print("Twoja waga jest w normie!")
elif bmi < 30:
    print("Masz nadwage!")
else:
    print("Jestes otyly!")


