# [WSI] - ćwiczenie 6

## Treść zadania
Proszę zaimplementować algorytm Q-Learning i użyć go do wyznaczenia polityki decyzyjnej dla problemu FrozenLake8x8-v0 (w wersji domyślnej, czyli z włączonym poślizgiem). W problemie chodzi o to, aby agent przedostał się przez zamarznięte jezioro z pozycji 'S' do pozycji 'G' unikając punktów 'H'. Symulator dla tego problemu można pobrać z podanej strony lub napisać własny o takiej samej funkcjonalności.

Oprócz zbadania domyślnego sposobu nagradzania (1 za dojście do celu, 0 w przeciwnym przypadku) proszę zaproponować własny system nagród i kar, po czym porównać osiągane wyniki z wynikami systemu domyślnego.

Za wynik uznajemy procent dojść do celu w 1000 prób. W każdej próbie można wykonać maksymalnie 200 akcji.

# Założenia

Algorytm nie posiada stałego parametru epsilon, tak jak było to zaprezentowane na wykładzie, jest on zmienny, zmniejsza się wykładniczo, czyli prawdopodobieństwo wybrania kierunku zmniejsza się z każdą kolejną krokiem. Takie rozwiązanie zapewnia dużo lepsze wyniki.

Parametry:
- β (learning rate) = `0.8`
- maksymalna liczba kroków = `200`
- γ (gamma) = `0.9`
- ε (epsilon) = (`1.0` ; `0.001`)
- decay rate = `0.00005`

Algorytm testowany jest w następujących warunkach:
- liczba epizodów = `1000`
- maksymalna liczba kroków = `200`
- liczba testów na daną ilość epizodów uczących = `30`

# Wyniki

default reward
- `1` pkt za dotarcie do celu, w przeciwnym wypadku `0`

Stały epsilon:
episodes | avg success
---------|------------
 1000    | 3.79%
 10000   | 7.97%
 50000   | 6.03%
 100000  | 5.09%
 250000  | 4.71%

episodes | avg success
---------|------------
 1000    | 2.11%
 10000   | 6.87%
 50000   | 28.37%
 100000  | 43.20%
 250000  | 57.91%

first reward
- `1` pkt za dotarcie do celu, `-1` za wpadnięcie do dziuwy, w przeciwnym wypadku `0`

episodes | avg success
---------|------------
 1000    | 3.81%
 10000   | 14.20%
 50000   | 45.81%
 100000  | 63.34%
 250000  | 68.93%

second reward
- `5` pkt za dotarcie do celu, `-1` za wpadnięcie do dziuwy, w przeciwnym wypadku `0`

episodes | avg success
---------|------------
 1000    | 3.80%
 10000   | 9.93%
 50000   | 37.32%
 100000  | 56.35%
 250000  | 72.57%

# Wnioski

Algorytm zachowuje się różnie w zależności od dobranych początkowych parametrów, jednakże po znalezieniu metodą inżynierską takowy algorytm zaczyna zachowywać się w dużo lepiej w sposób znaczący. Dodatkowo im większa ilość epizodów w trakcie nauki algorytmu, tym lepiej się on zachowuje. Zastosowanie różnych funkcji nagród zmienia wynik programu. Domyślna ewaluacja wypada najgorzej. Taka sama wartość nagrody i kary, długoterminowo (na kolejnych poziomach ilości epizodów) wypada dużo lepiej niż domyślna i druga funkcja nagrody, jednakże, druga funkcja nagrody, w której nagroda jest dużo większa niż kara, dla `250000` epizodów wypada znacznie lepiej.