[WSI] - ćwiczenie 2
=================

Treść zadania
------------
Zadanie\
Zaimplementować klasyczny algorytm ewolucyjny bez krzyżowania z selekcją turniejową i sukcesją elitarną. Dostępny budżet to 10000 ewaluacji funkcji celu. Optymalizujemy funkcję numer 4 z CEC 2017.

Uwaga\
Ponieważ algorytmy ewolucyjne wykorzystują losowość, nie wolno wyciągać wniosków na podstawie wyników pojedynczego uruchomienia. Należy porównywać średnie z co najmniej 25 uruchomień. W celu uzyskania pełnego obrazu, w tabelach z wynikami oprócz średniej zamieszcza się odchylenie standardowe, oraz najlepszy i najgorszy ze znalezionych wyników.

Pytania
------------
1.  Zbadać wpływ:
    - Siły mutacji
    - Rozmiaru elity
    - Liczby osobników w populacji

    na jakość uzyskanych rozwiązań.

2.  Jakie wnioski można wyciągnąć na podstawie wyników tego ćwiczenia?

Odpowiedzi
------------
1. Domyślne parametry:
    - liczby osobników w populacji = 20
    - siła mutacji = 1
    - rozmiar elity = 2
    - budżet = 10000
- Parametr - siła mutacji
```
|   Parametr |            min |            max |            avg |          std |
|------------|----------------|----------------|----------------|--------------|
|          0 | 400.0190103939 | 405.1408088829 | 400.4021457094 | 1.0569633038 |
|        0.1 | 400.0000000009 | 401.1241450571 | 400.1320714598 | 0.3629655587 |
|          1 | 400.0000000804 | 400.0000123460 | 400.0000021091 | 0.0000025876 |
|          2 | 400.0000001176 | 400.0000252619 | 400.0000082836 | 0.0000076691 |
|          5 | 400.0000037070 | 400.0001943352 | 400.0000381313 | 0.0000437186 |
|         10 | 400.0000013619 | 400.0003489142 | 400.0001073023 | 0.0000991737 |
|         25 | 400.0000115806 | 400.0030302773 | 400.0011642326 | 0.0010021876 |
|         50 | 400.0003598893 | 400.0099209474 | 400.0029305610 | 0.0024257732 |
|        100 | 400.0005887634 | 400.0246362815 | 400.0139310315 | 0.0086681017 |
```
- Parametr - rozmiar elity
```
|   Parametr |            min |            max |            avg |          std |
|------------|----------------|----------------|----------------|--------------|
|          0 | 400.0000022326 | 400.1157044225 | 400.0230228796 | 0.0306372174 |
|          1 | 400.0000000871 | 400.0000128661 | 400.0000027994 | 0.0000031052 |
|          2 | 400.0000002228 | 400.0000089534 | 400.0000035098 | 0.0000025442 |
|          5 | 400.0000000184 | 400.0000044017 | 400.0000013511 | 0.0000013814 |
|         10 | 400.0000000194 | 400.0000057389 | 400.0000020667 | 0.0000015582 |
|         15 | 400.0000000494 | 400.0000087822 | 400.0000020325 | 0.0000021903 |
|         20 | 400.0000000244 | 400.0000197067 | 400.0000026616 | 0.0000040786
```
- Parametr -  liczby osobników w populacji
```
|   Parametr |            min |            max |            avg |          std |
|------------|----------------|----------------|----------------|--------------|
|         10 | 400.0000000345 | 400.0000042529 | 400.0000013469 | 0.0000012866 |
|         20 | 400.0000000879 | 400.0000086739 | 400.0000022053 | 0.0000019238 |
|         50 | 400.0000000350 | 400.0000128851 | 400.0000030639 | 0.0000033719 |
|        100 | 400.0000000162 | 400.0000146262 | 400.0000031737 | 0.0000032872 |
|        250 | 400.0000004465 | 400.0000779843 | 400.0000101573 | 0.0000167496 |
|        500 | 400.0000016524 | 400.0002611663 | 400.0000318441 | 0.0000549131 |
|       1000 | 400.0000017647 | 400.0005421208 | 400.0000835037 | 0.0001126870 |
```
2. Wnioski:
    - W pierwszej tabeli (parametr - siła mutacji) jesteśmy w stanie zauważyć, że dla małej wartości siły mutacji algorytm odnajduje lepszą wartość minimum, mamy mniejsze odchylenie standardowe oraz średnia wartość jest zbliżona do minimum, niż gdy ustawimy dużą wartość siły mutacji, ale zbyt mała wartość mutacji posiada największą wartość maximum, ponieważ w zależności od początkowego rozrzucenia możemy nie przedostać w okolice minimum. Najlepiej sprawuje się siła mutacji od 1 do 2. Tak więc, niewielka siła mutacji oznacza dużą eksploatację (ale nie zbyt mała), a coraz większa wartość siły mutacji zmniejsza nam eksploatacje jednocześnie zwiększając eksploracje.
    - W drugiej tabeli, gdzie zmienialiśmy parametr - rozmiar elity, znacząco nie wypływa na wyniki, jedynie brak elity lub elita w rozmiarze populacji negatywnie wpływa na ostateczny wynik. W teorii coraz większy rozmiar elity wpływa negatywnie wpływa na odnajdowanie minimów. Zbyt duża elita może sprawić, że po dotarciu do minimum lokalnego zostaniemy w nim i nie odjedziemy minimum globalnego. W tym przypadku dobrze sprawuje się elita o rozmiarze od 1 do 5.
    - W trzeciej tabeli (parametr - liczba osobników w populacji) zaważamy, że najmniejsze wartości minimum odnajdują małe populacje, gorzej wypadają duże populacje. Wynika to z faktu iż duża populacja jest w stanie na początku pokryć większą część powierzchni, przez co szybciej na początku trafia w okolice minimum. Jednakże dla dużych populacji przez ograniczony budżet, nie jest w stanie odnaleźć najlepszego minimum (Mamy dużą eksplorację, a małą eksploatację), w przeciwieństwie do małej populacji, która odnalazła najlepsze minimum.


Autor
------------
Imię i Nazwisko: Mateusz Brzozowski\
Nr. Indeksu: 310608