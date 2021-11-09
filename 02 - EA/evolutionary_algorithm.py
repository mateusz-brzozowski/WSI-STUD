from cec2017.functions import f4
from random import randint, gauss
import numpy as np
from matplotlib import pyplot as plt
from itertools import product

_x_arr = _y_arr = np.arange(-120, 120, 5)
X, Y = np.meshgrid(_x_arr, _y_arr)
Z = np.empty(X.shape)
for i, j in product(range(X.shape[0]), range(X.shape[1])):
    Z[i, j] = f4(np.array([X[i, j], Y[i, j]]))



def evolutionary_algorithm(function, primary_popultion, population_size, mutation_factor, elite_size, t_max):
    t = 0
    rates = rate(function, primary_popultion)
    best_rate, best_member = find_best(primary_popultion, rates)
    population = primary_popultion.copy()
    while not stop(t, t_max, population, rates):
        reproduced_population = reproduction(population, rates, population_size)
        modificated_population = genetic_operations(reproduced_population, mutation_factor)
        modificated_rates = rate(function, modificated_population)
        member_rate, member = find_best(modificated_population, modificated_rates)
        if member_rate <= best_rate:
            best_rate = member_rate
            best_member = member
        population, rates = succession(population, modificated_population, rates, modificated_rates, elite_size)
        t+=1
    return best_member, best_rate

def rate(function, population):
    rate = []
    for member in population:
        rate.append(function(member))
    return rate

def find_best(population, rates):
    return min(zip(rates, population))


def stop(t, t_max, population, rate):
    if t >= t_max:
        return True
    return False

def reproduction(population, rate, population_size):
    new_population = []
    for i in range(population_size):
        oponent_id = randint(0, population_size - 1)
        if rate[i] <= rate[oponent_id]:
            new_population.append(population[i])
        else:
            new_population.append(population[oponent_id])
    return new_population


def genetic_operations(population, mutation_factor):
    modificated_population = []
    for member in population:
        point = []
        for variable in member:
            point.append(variable + gauss(0, 1) * mutation_factor)
        modificated_population.append(point)
    return modificated_population


def succession(population, modificate_population, rates, modificated_rates, elite_size):
    sorted_population = sorted(zip(rates, population))
    sorted_population = sorted_population[:elite_size]
    booth_population = sorted_population + list(zip(modificated_rates, modificate_population))
    booth_population = sorted(booth_population)
    new_population = []
    new_rates = []
    for rate, member in booth_population[:len(booth_population) - elite_size]:
        new_rates.append(rate)
        new_population.append(member)
    return new_population, new_rates

def main():
    UPPER_BOUND = 100
    DIMENSIONALITY = 2
    POPULATION_SIZE = 5
    BUDGET = 10000
    T_MAX = BUDGET // POPULATION_SIZE - 1
    MUTATION_FACTOR = 0.1
    ELITE_SIZE = 2
    for _ in range(5):
        population = []
        for _ in range(POPULATION_SIZE):
            population.append(list(np.random.uniform(-UPPER_BOUND, UPPER_BOUND, size=DIMENSIONALITY)))

        point, value = evolutionary_algorithm(f4, population, POPULATION_SIZE, MUTATION_FACTOR, ELITE_SIZE, T_MAX)
        print(point, value)

if __name__ == "__main__":
    main()
