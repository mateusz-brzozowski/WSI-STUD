# [WSI] - ćwiczenie 4

## Treść zadania
Zadanie\
Zaimplementować klasyfikator ID3 (drzewo decyzyjne). Atrybuty nominalne, testy tożsamościowe. Podać dokładność i macierz pomyłek na zbiorach: Breast cancer i mushroom. Sformułować i spisać w kilku zdaniach wnioski.

### Poniżej kilka wskazówek ogólnych do tego ćwiczenia
- Atrybuty nominalne - każdy atrybut może przyjmować jedną z kilku dozwolonych wartości, zakładamy, że wartość atrybutu to napis, np. "kot", "a", "20-34", ">40".
- Testy tożsamościowe - jeżeli atrybut testowany w danym węźle ma np. 3 dozwolone wartości, np. a, b, c, to z węzła tego wychodzą 3 krawędzie oznaczone: a, b, c.
- Na tym ćwiczeniu klasyfikator trenuje się na zbiorze trenującym, a ocenia jego jakość na zbiorze testującym. Należy losowo podzielić zbiór danych na trenujący i testujący w stosunku 3:2.
- Jeżeli zbiór danych zawiera numery lub identyfikatory wierszy to należy je wyrzucić - nie chcemy uczyć się identyfikatorów wierszy.
- Brakujące wartości atrybutów taktujemy jako wartość, np. jeżeli symbol ‘?’ oznacza brakującą wartość, a symbole ‘a’, ‘b’ wartości normalne, to z naszego punktu widzenia mamy 3 wartości normalne (fachowo: 3 wartości atrybutu): ‘a’, ‘b’, ‘?’.
- Tak na prawdę to nie musimy rozumieć dziedziny problemu - na wejściu mamy napisy, na wyjściu napisy, nie ważne czy klasyfikujemy sekwencje DNA, grzyby, czy samochody.
- Nazwa pliku ze zbiorem danych jest parametrem algorytmu klasyfikacji, kod klasyfikatora powinien być w stanie obsłużyć inny zbiór danych o tym samym rozkładzie kolumn (czyli nie należy wpisywać wartości atrybutów „na sztywno” w kodzie).
- W repozytorium ze zbiorami danych zwykle w plikach „.names” jest napisane, który atrybut to klasa (czyli wartości której kolumny mamy się nauczyć przewidywać).

# Dokładność i macierz pomyłek

## Breast Cancer

Liczba rekordów: `286`\
Liczba zmiennych: `10`

expected / predicted | positive | negative
---------------------|----------|---------
positive             | 12.79    | 21.18
negative             | 19.62    | 61.41

AVG: `0.6447826086956522`

## Mushroom

Liczba rekordów: `8124`\
Liczba zmiennych: `22`

expected / predicted | positive | negative
---------------------|----------|---------
positive             | 1682.34  | 0
negative             | 0        | 1567.66

AVG: `1.0`

## Tic-Tac-Toe

Liczba rekordów: `958`\
Liczba zmiennych: `10`

expected / predicted | positive | negative
---------------------|----------|---------
positive             | 220.28   | 29.82
negative             | 32.13    | 101.77

AVG: `0.838671875`

# Wnioski

Algorytm zachosuje sie różnie w zależności od ilości rekordów w zbiorze danych, w zależności od ilości atrybutów oraz dobraniu odpowiednich par uczących:
- Dla zbiorów danych gdzie mamy bardzo dużo rekordów oraz durzą liczbę atrybutów (zbiór `Mushroom`) algorytm zbudował drzewo, które działa ze `100%` skutecznością, Tak więc im więcej par uczących, więcej ilości danych w zbiorze, więcej atrybutów (ale też nie za dużo) algorytm działa dużo lepiej.
- W zbiorze `Tic-Tac-Toe` i `Breast Cancer` mamy taką samą ilość argumentów, jendakże zbiór `Tic-Tac-Toe` zachowywuje sie znacznie lepiej od zbioru `Breast Cancer`, ponieważ znajduje się w nim ponad trzy razy więcej rekordów danych, dzięki czemu mamy więcej par uczących i algorytm działa skuteczniej. Tak więc dla mniejszych zbiorów skuteczność zależy od doboru par uczących, czyli od tego które pary uczące na początku wybierzemy.