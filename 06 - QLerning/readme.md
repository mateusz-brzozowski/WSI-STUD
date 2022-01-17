# [WSI] - ćwiczenie 6

## Treść zadania
Proszę zaimplementować algorytm Q-Learning i użyć go do wyznaczenia polityki decyzyjnej dla problemu FrozenLake8x8-v0 (w wersji domyślnej, czyli z włączonym poślizgiem). W problemie chodzi o to, aby agent przedostał się przez zamarznięte jezioro z pozycji 'S' do pozycji 'G' unikając punktów 'H'. Symulator dla tego problemu można pobrać z podanej strony lub napisać własny o takiej samej funkcjonalności.

Oprócz zbadania domyślnego sposobu nagradzania (1 za dojście do celu, 0 w przeciwnym przypadku) proszę zaproponować własny system nagród i kar, po czym porównać osiągane wyniki z wynikami systemu domyślnego.

Za wynik uznajemy procent dojść do celu w 1000 prób. W każdej próbie można wykonać maksymalnie 200 akcji.

# Wyniki

default_reward

episodes | avg success
---------|------------
 1000    | 2.11%
 10000   | 6.87%
 50000   | 28.37%
 100000  | 43.20%
 250000  | 57.91%

first_reward

episodes | avg success
---------|------------
 1000    | 3.81%
 10000   | 14.20%
 50000   | 45.81%
 100000  | 63.34%
 250000  | 68.93%

second_reward

episodes | avg success
---------|------------
 1000    | 3.80%
 10000   | 9.93%
 50000   | 37.32%
 100000  | 56.35%
 250000  | 72.57%

# Wnioski
