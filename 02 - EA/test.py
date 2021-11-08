from evolutionary_algorithm import evolutionary_algorithm
from cec2017.functions import f4
from statistics import mean, stdev
from tabulate import tabulate
import numpy as np



def test(population_size, mutation_factor, elite_size, t_max, parameter):
    UPPER_BOUND = 100
    DIMENSIONALITY = 2
    population = []
    values = []
    for _ in range(25):
        for _ in range(population_size):
            population.append(list(np.random.uniform(-UPPER_BOUND, UPPER_BOUND, size=DIMENSIONALITY)))
        point, value = evolutionary_algorithm(f4, population, population_size, mutation_factor, elite_size, t_max)
        values.append(value)
    return [parameter, min(values), max(values), mean(values), stdev(values)]

def main():
    HEADER = ["Parametr", "min", "max", "avg", "std"]
    POPULATION_SIZES = [10, 20, 50, 100, 250, 500, 1000]
    BUDGET = 10000
    MUTATION_FACTORS = [0, 0.1, 1, 2, 5, 10, 25, 50, 100]
    ELITE_SIZES = [0, 1, 2, 5, 10, 15, 20]

    # rows = []
    # for population_size in POPULATION_SIZES:
    #     t_max = BUDGET // population_size - 1
    #     rows.append(test(population_size, 0.1, 2, t_max, population_size))
    # print(tabulate(rows, headers=HEADER, tablefmt="github", floatfmt=".10f"))

    rows = []
    for mutation_factor in MUTATION_FACTORS:
        t_max = BUDGET // 20 - 1
        rows.append(test(20, mutation_factor, 2, t_max, mutation_factor))
    print(tabulate(rows, headers=HEADER, tablefmt="github", floatfmt=".10f"))

    # rows = []
    # for elite_size in ELITE_SIZES:
    #     t_max = BUDGET // 20 - 1
    #     rows.append(test(20, 0.1, elite_size, t_max, elite_size))
    # print(tabulate(rows, headers=HEADER, tablefmt="github", floatfmt=".10f"))

if __name__ == "__main__":
    main()
