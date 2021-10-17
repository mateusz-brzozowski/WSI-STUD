[WSI] - ćwiczenie 1
=================

Treść zadania
------------
Zadanie na pierwsze spotkanie:\
Mamy problem plecakowy jak na wykładzie:\
w = np.array([8, 3, 5, 2]) #waga przedmiotów\
W = 9 #maksymalna waga plecaka\
p = np.array([16, 8, 9, 6]) #wartość przedmiotów
1.  Znaleźć rozwiązanie optymalne przez przegląd wyczerpujący
2.  Rozwiązać problem przy użyciu heurystyki: do plecaka pakujemy przedmioty według kolejności wynikającej ze stosunku p/w

Pytania
------------
1.  Czy uzyskano takie same rozwiązania?
2.  Jakie wnioski można z tego wyciągnąć?
3.  Jak dużą instancję problemu (liczba przedmiotów) da się rozwiązać w około minutę metodą zachłanną?
4.  Jak bardzo wydłuży obliczenia dodanie jeszcze jednego przedmiotu?

Odpowiedzi
------------
1.	Nie, rozwiązania różnią się między sobą. W przeglądzie wyczerpującym użyliśmy 2 i 3 element i uzyskaliśmy wartość równą 19. Natomiast przy użyciu heurystyki użyliśmy 2 i 4 element i uzyskaliśmy wartość równą 14.
2.	Zastosowanie "rad dobrej wróżki", czyli odpowiedniej heurystyki pozwala nam na uzystanie wyniku, który w naszym przypadku nie jest najlepszym z możliwym, jednakże jest to jedno z lepszych ustawień przemiotów w plecaku.
3.	Dla metody zachłannej w średnimm czasie 49,39 sekund udało się sprawdzić 24 przedmioty.
4.	Dodanie jednego elementu spowodowało wydłużenie czasu średnio o 64,09 sekund.

Autor
------------
Imię i Nazwisko: Mateusz Brzozowski\
Nr. Indeksu: 310608