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
|          0 | 400.1495427209 | 405.3873343659 | 400.4364844888 | 1.0892966809 |
|        0.1 | 400.0000264864 | 404.7152160674 | 400.8707408982 | 1.4705526015 |
|          1 | 400.0000096531 | 401.5993211851 | 400.1314423245 | 0.3858817458 |
|          2 | 400.0000020627 | 400.0001075148 | 400.0000292724 | 0.0000304517 |
|          5 | 400.0000065868 | 400.0277922750 | 400.0075844412 | 0.0080689576 |
|         10 | 400.0000639078 | 400.0183603971 | 400.0048586049 | 0.0044414152 |
|         25 | 400.0001844568 | 400.0153058984 | 400.0039136335 | 0.0037233915 |
|         50 | 400.0031619947 | 400.1219359753 | 400.0262081551 | 0.0315451993 |
|        100 | 400.0023448065 | 401.0267443589 | 400.0942700046 | 0.1994527749 |
```
- Parametr - rozmiar elity
```
|   Parametr |            min |            max |            avg |          std |
|------------|----------------|----------------|----------------|--------------|
|          0 | 400.0488584795 | 401.3150068062 | 400.3108040269 | 0.2966468263 |
|          1 | 400.0005898854 | 402.3534137120 | 400.1825508783 | 0.6047470761 |
|          2 | 400.0000001783 | 400.0211977284 | 400.0054481529 | 0.0085922422 |
|          5 | 400.0000004686 | 404.8175552826 | 400.2716851695 | 0.9513914900 |
|         10 | 400.0298975974 | 414.4839385068 | 401.4381446099 | 3.2766847187 |
|         15 | 400.0000000173 | 400.1843760833 | 400.0216880981 | 0.0519860117 |
|         20 | 400.0060428587 | 409.5465715740 | 400.6031431836 | 1.8957432347 |
```
- Parametr -  liczby osobników w populacji
```
|   Parametr |            min |            max |            avg |          std |
|------------|----------------|----------------|----------------|--------------|
|         10 | 400.0000019258 | 400.0748107383 | 400.0251324353 | 0.0204154446 |
|         20 | 400.0022071892 | 402.8246157443 | 400.3013824521 | 0.7201820418 |
|         50 | 400.0104039483 | 401.8714617238 | 400.2640551719 | 0.4846047036 |
|        100 | 400.0008793426 | 400.2034566892 | 400.0455728817 | 0.0508018398 |
|        250 | 400.0098391397 | 400.0781275279 | 400.0160131300 | 0.0170608014 |
|        500 | 400.0013350858 | 400.0108437269 | 400.0050578270 | 0.0039432673 |
|       1000 | 400.0035324942 | 400.0181218601 | 400.0057546901 | 0.0029242665 |
```
2. Wnioski:
    - W pierwszej tabeli (parametr - siła mutacji) jesteśmy w stanie zauważyć, że dla małej wartości siły mutacji algorytm odnajduje lepszą wartość minimum, mamy mniejsze odchylenie standardowe oraz średnia wartość jest zbliżona do minimum, niż gdy ustawimy dużą wartość siły mutacji. Tak więc, niewielka siła mutacji oznacza dużą eksploatację (ale nie zbyt mała), a coraz większa wartość siły mutacji zmniejsza nam eksploatacje jednocześnie zwiększając eksploracje.
    - W drugiej tabeli, gdzie zmienialiśmy parametr - rozmiar elity, nie odnajduję zadanej zależności. W teorii coraz większy rozmiar elity wpływa negatywnie na odnajdowanie minimów. Zbyt duża elita może sprawić, że po dotarciu do minimum lokalnego zostaniemy w nim i nie odjedziemy minimum globalnego.
    - W trzeciej tabeli (parametr - liczba osobników w populacji) zaważamy, że wraz ze wzrostem populacji maleje odchylenie standardowe oraz średnia wyników. Wynika to z faktu iż duża populacja jest w stanie na początku pokryć większą część powierzchni, przez co szybciej na początku trafia w okolice minimum. Jednakże dla dużych populacji przez ograniczony budżet, nie jest w stanie odnaleźć najlepszego minimum (Mamy dużą eksplorację, a małą eksploatację), w przeciwieństwie do małej populacji, która odnalazła najlepsze minimum.


Autor
------------
Imię i Nazwisko: Mateusz Brzozowski\
Nr. Indeksu: 310608