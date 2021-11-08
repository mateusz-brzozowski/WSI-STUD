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
    - siła mutacji = 0.1
    - rozmiar elity = 2
    - budżet = 10000
- Parametr - siła mutacji
```
|   Parametr |            min |            max |            avg |          std |
|------------|----------------|----------------|----------------|--------------|
|          0 | 400.0250965636 | 402.2814158826 | 400.9644389275 | 0.9254354175 |
|        0.1 | 400.0316121840 | 413.7964935186 | 401.0426446566 | 3.0258228280 |
|          1 | 400.0008624176 | 400.1080479024 | 400.0269521459 | 0.0386293914 |
|          2 | 400.0029443788 | 400.0331110887 | 400.0280083465 | 0.0075670102 |
|          5 | 400.0002401701 | 400.1512869619 | 400.0292964541 | 0.0457137235 |
|         10 | 400.0002973226 | 400.0148259803 | 400.0096122353 | 0.0061854215 |
|         25 | 400.0000080242 | 400.0048387200 | 400.0007871013 | 0.0010161963 |
|         50 | 400.0012776766 | 400.1418437910 | 400.0269885648 | 0.0392690902 |
|        100 | 400.0129462407 | 401.0478191034 | 400.3454216449 | 0.3074151026 |
```
- Parametr - rozmiar elity
```
|   Parametr |            min |            max |            avg |          std |
|------------|----------------|----------------|----------------|--------------|
|          0 | 400.0305685706 | 409.1244739408 | 400.4269878542 | 1.8135727637 |
|          1 | 400.1250743490 | 400.3952934170 | 400.2199487178 | 0.0821171206 |
|          2 | 400.0000000029 | 400.0002842419 | 400.0000118722 | 0.0000567631 |
|          5 | 400.0000000068 | 400.0327887981 | 400.0050067580 | 0.0094208473 |
|         10 | 400.0844685699 | 404.0260364258 | 400.5885485796 | 1.2626195371 |
|         15 | 400.0294362129 | 400.5846570207 | 400.4274995833 | 0.1551975734 |
|         20 | 400.0091370842 | 400.2292389969 | 400.1155754458 | 0.0626046347 |
```
- Parametr -  liczby osobników w populacji
```
|   Parametr |            min |            max |            avg |          std |
|------------|----------------|----------------|----------------|--------------|
|         10 | 400.0000000016 | 400.0000001065 | 400.0000000266 | 0.0000000266 |
|         20 | 400.0000000128 | 400.0814438841 | 400.0500151309 | 0.0190078276 |
|         50 | 400.0001319405 | 400.9431065074 | 400.1065714993 | 0.2309082198 |
|        100 | 400.0000000005 | 400.0094050723 | 400.0016346720 | 0.0025646885 |
|        250 | 400.0000000000 | 400.0000000027 | 400.0000000009 | 0.0000000008 |
|        500 | 400.0000000000 | 400.0000000026 | 400.0000000007 | 0.0000000007 |
|       1000 | 400.0000000454 | 400.0282366442 | 400.0045276396 | 0.0065409357 |
```
2. Wnioski:

Autor
------------
Imię i Nazwisko: Mateusz Brzozowski\
Nr. Indeksu: 310608