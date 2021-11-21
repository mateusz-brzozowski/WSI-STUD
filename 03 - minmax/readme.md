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
-
```
| White_Depth / Blue_Depth | 1        | 2        | 3        | 4        | 5        |
| ------------------------ | -------- | -------- | -------- | -------- | -------- |
| 1                        | Blue | White | Draw | Draw | Blue |
| 2                        | White | Draw | Draw | Draw |  |
| 3                        | White | White |  |  |  |
| 4                        | White | Draw |  |  |  |
| 5                        | White | White |  |  |  |
```
-

2. Wnioski:
    -


Autor
------------
Imię i Nazwisko: Mateusz Brzozowski\
Nr. Indeksu: 310608
