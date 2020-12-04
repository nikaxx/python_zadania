"""
### Zadanie 2.5 Zamiana elementów na liście
Napisz program zamieniający miejscami w zadanej liście liczb element
największy z najmniejszym.
na wejsciu: [49, 50, 20, 40, 35, 10]
na wyjsciu: [49, 10, 20, 40, 35, 50]

Jak to zrobimy?
1. Musimy znaleźć indeks elementu o największej wartosci
i indeks elementu o najmniejszej wartości
2. Zamiana miejscami elementów z tych indeksów

Wersja A
1. używamy pętli for do znalezienia indeksów
2. Zamieniamy wartości pod tymi indeksami

Wersja B
1. Używając funkcji min(), max() znajduje najmniejszą i najwieksza wartosc
2. Znajduję indeks tych elementów w liscie
3. Zamieniam te elementy miejscami

"""
liczby = [49, 50, 20, 40, 35, 10]
print(f'Lista wejsciowa to: {liczby}')
minimum = min(liczby)
maximum = max(liczby)
index_maximum = liczby.index(maximum)
index_minimum = liczby.index(minimum)
liczby[index_maximum], liczby[index_minimum] = liczby[index_minimum], liczby[index_maximum]
print(f'Lista wyjsciowa to: {liczby}')
