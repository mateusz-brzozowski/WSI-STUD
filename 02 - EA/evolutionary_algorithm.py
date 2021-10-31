from cec2017.functions import f4
import numpy as np
from random import randint


def evolutionary_algorithm(function, primary_popultion, population_size, mutation_factor, elite_size, t_max):
    t = 0
    rates = rate(function, primary_popultion)
    best_member, best_rate = find_best(primary_popultion, rates)
    population = [primary_popultion]
    members = []
    members_rate = []
    while not stop(t, t_max, population[t], rates):
        reproduced_population = reproduction(population[t], rates, population_size)
        modificated_population = genetic_operations(reproduced_population, mutation_factor)
        modificated_rates = rate(function, modificated_population)
        members[t], members_rate[t] = find_best(modificated_population, modificated_rates)
        if rates[t] <= best_rate:
            best_rate = members_rate[t]
            best_member = members[t]
        population[t+1], best_rate = succession(population[t], modificated_population, rates, modificated_rates, elite_size)
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
        if rate[i] <= rate[-i]:
            new_population.append(population[i])
        else:
            new_population.append(population[-i])
    return new_population


def genetic_operations(population, mutation_factor):
    for member in population:
        for x in member:
            x + randint(0, 1) * mutation_factor


def succession(population, modificate_population,  rates, modificated_rates, elite_size):
    pass


def main():
    UPPER_BOUND = 100
    DIMENSIONALITY = 2
    POPULATION_SIZE = 20
    T_MAX = 10000
    MUTATION_FACTOR = 1.0
    ELITE_SIZE = 1
    population = []
    for _ in range(20):
        population.append(np.random.uniform(-UPPER_BOUND, UPPER_BOUND, size=DIMENSIONALITY))

    evolutionary_algorithm(f4, population, POPULATION_SIZE, MUTATION_FACTOR, ELITE_SIZE, T_MAX)

if __name__ == "__main__":
    main()
