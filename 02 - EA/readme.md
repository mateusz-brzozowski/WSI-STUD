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
  Parametr      min      max      avg          std
----------  -------  -------  -------  -----------
       0    400.022  400.475  400.156  0.135771
       0.1  400.016  400.047  400.027  0.00529309
       1    400      400.187  400.025  0.0511566
      10    400      400.001  400      0.000360913
      50    400      400.006  400.002  0.00174764
     100    400.011  400.139  400.077  0.0287827
```
- Parametr - rozmiar elity
```
  Parametr      min      max      avg          std
----------  -------  -------  -------  -----------
         0  400      400      400      7.65509e-08
         1  400.011  401.182  400.163  0.247173
         2  400      400.048  400.004  0.0125163
         5  400      402.82   400.132  0.560678
        10  400      400.031  400.001  0.00622761
        15  400.001  404.113  400.22   0.812313
```
- Parametr -  liczby osobników w populacji
```
  Parametr      min      max      avg          std
----------  -------  -------  -------  -----------
        10  400      400.132  400.043  0.0413142
        20  400.116  402.941  400.828  0.813332
        30  400.044  404.751  400.784  1.3506
        40  400      400      400      1.96792e-09
        50  400.002  400.212  400.036  0.053583
       100  400      400.001  400      0.000149499
```
2. Wnioski:

Autor
------------
Imię i Nazwisko: Mateusz Brzozowski\
Nr. Indeksu: 310608