"""
### Zadanie 1.9 FizzBuzz
Napisz program, który wyświetla liczby od 1 do 100.
Dla liczb podzielnych przez 3 niech program wyświetli `Fizz`;
dla liczb podzielnych przez 5 niech wyświetli `Buzz`;
a dla liczb podzielnych przez 15 niech wyświetli `FizzBuzz`.
"""
for liczba in range(1, 101):
    print(liczba, end ='')
    if liczba % 15 == 0:
        print(' - FizzBuzz')
    elif liczba % 3 == 0:
        print(' - Fizz')
    elif liczba % 5 == 0:
        print(' - Buzz')
    else:
        print(' ')