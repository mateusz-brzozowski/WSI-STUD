[WSI] - ćwiczenie 3
=================

Treść zadania
------------
Zadanie\
Zaimplementować algorytm min-max z przycinaniem alfa-beta. Algorytm ten należy zastosować do gry w proste warcaby (checekers/draughts). Niech funkcja oceny planszy zwraca różnicę pomiędzy stanem planszy gracza a stanem przeciwnika. Za pion przyznajemy 1 punkt, za damkę 10 p.

Przygotowałem dla Państwa kod, który powinien ułatwić wykonanie zadania. Zamiast mojego kodu, osoby chętne mogą napisać własny kod pomocniczy. Nie można używać kodu z Internetu, czy bardziej ogólnie, kodu, którego nie jest się autorem.

Wiem co jest dostępne w Internecie, większość dostępnych implementacji ma cechy szczególne, po których łatwo je rozpoznać.

Zasady gry (w skrócie: wszyscy ruszają się po 1 polu. Pionki tylko w kierunku wroga, damki w dowolnym) z następującymi modyfikacjami:

- bicie nie jest wymagane
- dozwolone jest tylko pojedyncze bicie (bez serii).

Pytania
------------
- Czy gracz sterowany przez AI zachowuje się rozsądnie z ludzkiego punktu widzenia? Jeśli nie to co jest nie tak?

Niech komputer gra z komputerem (bez wizualizacji), zmieniamy parametry jednego z oponentów, badamy jak zmiany te wpłyną na liczbę jego wygranych. Należy zbadać wpływ:

- Głębokości drzewa przeszukiwań
- Alternatywnych funkcji oceny stanu, np.:
    1. nagrody jak w wersji podstawowej + nagroda za stopień zwartości grupy (jak wszyscy blisko siebie to OK, no chyba, że da się coś zabrać przeciwnikowi)
    2. za każdy pion na własnej połowie planszy otrzymuje się 5 nagrody, na połowie przeciwnika 7, a za każdą damkę 10.
    3. za każdy nasz pion otrzymuje się nagrodę w wysokości: (5 + numer wiersza, na którym stoi pion) (im jest bliżej wroga tym lepiej), a za każdą damkę: 10.

Odpowiedzi
------------
1. Tabele
- Domyślna ewaluacja +10 za damkę +1 za pion
```
| White_Depth / Blue_Depth | 1     | 2     | 3     | 4     | 5     |
| ------------------------ | ----- | ----- | ----- | ----- | ----- |
| 1                        | Blue  | White | Draw  | Draw  | Blue  |
| 2                        | White | Draw  | Draw  | Draw  | Draw  |
| 3                        | White | White | White | Draw  | Draw  |
| 4                        | White | Draw  | Draw  | Draw  | Draw  |
| 5                        | White | White | White | Draw  | White |
```
- Ewaluacja +10 za damkę +5 za piona na swojej połowie +7 za piona na połowie przeciwnika
```
| White_Depth / Blue_Depth | 1     | 2     | 3     | 4     | 5     |
| ------------------------ | ----- | ----- | ----- | ----- | ----- |
| 1                        | White | Blue  | Blue  | Draw  | Blue  |
| 2                        | White | White | Draw  | Draw  | Draw  |
| 3                        | White | Draw  | Draw  | Draw  | Blue  |
| 4                        | White | Draw  | White | Draw  | White |
| 5                        | White | White | Draw  | Draw  | Draw  |
```
- Ewaluacja +10 za damkę +5 za piona + kolumna
```
| White_Depth / Blue_Depth | 1     | 2     | 3     | 4     | 5     |
| ------------------------ | ----- | ----- | ----- | ----- | ----- |
| 1                        | Blue  | Blue  | Draw  | Blue  | Blue  |
| 2                        | White | Draw  | Draw  | White | Draw  |
| 3                        | White | White | White | Draw  | Draw  |
| 4                        | White | Draw  | Draw  | Draw  | Blue  |
| 5                        | White | White | White | Draw  | Blue  |
```
- Dla bialych i niebieskich głębokość przeszukiwać równa 5
    - evaluate - domyślna ewaluacja
    - evaluate2 - premiowanie połowy przeciwnika
    - evaluate3 - premiowanie odległości od startu
    - evaluate4 - premiowanie zwartości grupy
```
| White_Eval/ Blue_Eval | evaluate  | evaluate2 | evaluate3 | evaluate4 |
| --------------------- | --------- | --------- | --------- | --------- |
| evaluate              | White     | Draw      | Draw      | Draw      |
| evaluate2             | White     | Draw      | Draw      | Draw      |
| evaluate3             | Draw      | Blue      | Blue      | Draw      |
| evaluate4             | Draw      | Draw      | Draw      | Draw      |
```

2. Wnioski:
    - Jeżeli chodzi o grę człowiek vs komputer, Algorytm przy głębokości równej 5 i podstawowej ewaluacji zachowuje się w sposób logiczny. Nie wystawia się na bicie. Kiedy może zbić pionka zbija go, jendakże kiedy zbicie nie ma sensu, ponieważ może wiecej stacić nie robi tego, ale kiedy komputer zauważy możliwość "zrobienia" damki jest w stanie poświęcić pionki, byle by uzyskać damkę, która jest dużo warta, tak też wynika z założonej heurystyki.

    - Komputer vs Komputer. W tym przypadku analiza wyników jest utrudniona, ponieważ komputer nie potrafi rozgrywać "koncówek". Wynika to z poziomu głębokości, kiedy przechodzimy do ostatniego etapu rozgrywki przewidywanie 5 ruchów do przodu, a nawet więcej nic nie da, ponieważ odległości pomiędzy damkami potrafią wynosić 7 ruchów (w szachach stosuje się schematy rozgywania "koncówek", ponieważ należy wykonać 15-20 ruchów które są schematyczne i nie ma potrzeby obliczania każdej możliwej kombinacji)

    - Z porównywania głębokości dla każdej z ewaluacji jesteśmy wywnioskować, że osoba z dużo lepszą głębokością (poza podstawową ewaluacją) zazwyczaj wygrywa. Jadnak dla głębokości 4 i 5 różnice się zacierają i rozgrywki kończą się remisem. Dodatkowo zazwyczaj wygrywa osoba rozpoczynająca rozgrywkę.

    - Porównywanie różnych ewaluacji jest utrudnione ze względu na to o czym wspomniałem w punkcie drugim. Jedyny wniosek jest taki, że ewaluacja premiująca znajdowanaie się pionków na połowie przeciwnika jest lepsza od pozostałych.

Autor
------------
Imię i Nazwisko: Mateusz Brzozowski\
Nr. Indeksu: 310608
