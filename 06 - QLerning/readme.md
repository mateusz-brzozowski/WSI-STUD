# [WSI] - ćwiczenie 6

## Treść zadania
Proszę zaimplementować algorytm Q-Learning i użyć go do wyznaczenia polityki decyzyjnej dla problemu FrozenLake8x8-v0 (w wersji domyślnej, czyli z włączonym poślizgiem). W problemie chodzi o to, aby agent przedostał się przez zamarznięte jezioro z pozycji 'S' do pozycji 'G' unikając punktów 'H'. Symulator dla tego problemu można pobrać z podanej strony lub napisać własny o takiej samej funkcjonalności.

Oprócz zbadania domyślnego sposobu nagradzania (1 za dojście do celu, 0 w przeciwnym przypadku) proszę zaproponować własny system nagród i kar, po czym porównać osiągane wyniki z wynikami systemu domyślnego.

Za wynik uznajemy procent dojść do celu w 1000 prób. W każdej próbie można wykonać maksymalnie 200 akcji.

# Założenia

Parametry:
- β (learning rate) = `0.06`
- maksymalna liczba kroków = `200`
- γ (gamma) = `0.9`
- ε (epsilon) = `0.8`
- decay rate = `0.00005`

Algorytm testowany jest w następujących warunkach:
- liczba epizodów = `1000`
- maksymalna liczba kroków = `200`
- liczba testów na daną ilość epizodów uczących = `30`

# Wyniki

default reward
- `1` pkt za dotarcie do celu, w przeciwnym wypadku `0`

episodes | avg success
---------|------------
 1000    | 1.11%
 5000    | 15.87%
 10000   | 27.37%
 25000   | 38.20%
 50000   | 52.91%


first reward
- `1` pkt za dotarcie do celu, `-1` za wpadnięcie do dziuwy, w przeciwnym wypadku `0`

episodes | avg success
---------|------------
 1000    | 15.20%
 5000    | 65.35%
 10000   | 71.50%
 25000   | 79.85%
 50000   | 80.75%

second reward
- `5` pkt za dotarcie do celu, `-1` za wpadnięcie do dziuwy, w przeciwnym wypadku `0`

episodes | avg success
---------|------------
 1000    | 26.65%
 5000    | 38.55%
 10000   | 47.50%
 25000   | 70.40%
 50000   | 76.95%

# Wnioski

Algorytm zachowuje się różnie w zależności od dobranych początkowych parametrów, jednakże po znalezieniu metodą inżynierską takowy algorytm zaczyna zachowywać się w dużo lepiej w sposób znaczący. Dodatkowo im większa ilość epizodów w trakcie nauki algorytmu, tym lepiej się on zachowuje. Zastosowanie różnych funkcji nagród zmienia wynik programu. Domyślna ewaluacja wypada najgorzej. Taka sama wartość nagrody i kary wypada dużo lepiej niż domyślna i trochę lepiej, niż druga funkcja nagrody, w której nagroda jest dużo większa niż kara. Aczkolwiek dla mniejszych zbiorów, druga funckja nagrody wypada prawie 2 razy lepiej, jendkaże potem wynik rośinie dużo wolniej, niż pierwsza funckja nagrody.