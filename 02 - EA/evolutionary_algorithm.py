def evolutionary_algorithm(function, primary_popultion, strenght, t_max):
    t = 0
    o = rate(function, primary_popultion)
    x_g, o_g = find_best(primary_popultion, o)
    population = [primary_popultion]
    while not stop(t, t_max, population[t], o):
        current_population = reproduction(population[t], o, strenght)
        modificate_population = tournament(current_population)
        o_m = rate(function, modificate_population)
        x[t], o[t] = find_best(modificate_population, o_m)
        if o[t] <= o_g:
            o_g = o[t]
            x_g = x[t]
        population[t+1], o = succession(population[t], modificate_population,  o, o_m)
        t+=1
    return x_g, o_g

def rate(function, population):
    pass

def find_best(population, rate):
    pass

def stop(t, t_max, population, rate):
    pass

def reproduction(population, rate, strenght):
    pass

def tournament(population):
    pass

def succession(population, modificate_population,  o, o_m):
    pass

def main():
    pass

if __name__ == "__main__":
    main()
