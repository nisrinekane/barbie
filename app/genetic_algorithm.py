import os
import random
from deap import base, creator, tools
import numpy as np
from image_processing import generate_img, calculate_difference
from PIL import Image
import matplotlib.pyplot as plt
from config import POINT_COUNT, POPULATION_SIZE, ELITE_SIZE

SAVE_DIR = "saved_images"
os.makedirs(SAVE_DIR, exist_ok=True)
target_img = Image.open('barbie_logo.jpg')

# define the fitness 
creator.create('FitnessMax', base.Fitness, weights=(1.0,))
creator.create('Individual', list, fitness=creator.FitnessMax)

toolbox = base.Toolbox()

# attribute generator
toolbox.register('attr_point', lambda: (random.uniform(0, 1), random.uniform(0, 1), random.uniform(0, 1)))

# structure initializers
toolbox.register('individual', tools.initRepeat, creator.Individual, toolbox.attr_point, n=POINT_COUNT)
toolbox.register('population', tools.initRepeat, list, toolbox.individual, n=POPULATION_SIZE)

population = toolbox.population()

def evaluate(individual):
    individual_img = generate_img(individual)
    score = calculate_difference(individual_img, target_img)
    return (score,)


def mutate(individual, indpb):
    # small random change to each point in the individual with a probability of indpb.
    for i in range(len(individual)):
        if random.random() < indpb:
            individual[i] = toolbox.attr_point()
    return individual,

def mate(individual1, individual2):
    # perform one point crossover
    crossover_point = random.randint(1, len(individual1) - 1)
    individual1[crossover_point:], individual2[crossover_point:] = individual2[crossover_point:], individual1[crossover_point:]
    return individual1, individual2

toolbox.register("evaluate", evaluate)
toolbox.register("mate", mate)
toolbox.register("mutate", mutate, indpb=0.05)
toolbox.register("select", tools.selTournament, tournsize=3)

#  main loop:
NGEN = 10000
for gen in range(NGEN):
    # select and clone next generation individuals
    offspring = toolbox.select(population, len(population) - ELITE_SIZE)
    offspring = list(map(toolbox.clone, offspring))

    # apply crossover 
    for child1, child2 in zip(offspring[::2], offspring[1::2]):
        toolbox.mate(child1, child2)
        del child1.fitness.values, child2.fitness.values

    # apply mutation
    for mutant in offspring:
        toolbox.mutate(mutant)
        del mutant.fitness.values

    # evaluate individuals:
    invalids = [ind for ind in offspring if not ind.fitness.valid]
    fitnesses = map(toolbox.evaluate, invalids)
    for ind, fit in zip(invalids, fitnesses):
        ind.fitness.values = fit

    # Elitism: get the best individuals from the past generation
    elite = sorted(population, key=lambda ind: ind.fitness.values, reverse=True)[:ELITE_SIZE]

    # replace population with the offspring and elite
    population[:] = offspring + elite

    # visualize best individual from current generation
    best_ind = tools.selBest(population, 1)[0]
    best_img = generate_img(best_ind)
    # save only every 500th image
    if gen % 500 == 0:
        best_img.save(os.path.join(SAVE_DIR, f"gen_{gen}.png"))

    # print stats
    print(f"generation: {gen}")

    # apply crossover 
    for child1, child2 in zip(offspring[::2], offspring[1::2]):
        toolbox.mate(child1, child2)
        del child1.fitness.values, child2.fitness.values

    # apply mutation
    for mutant in offspring:
        toolbox.mutate(mutant)
        del mutant.fitness.values

    # evaluate individuals:
    invalids = [ind for ind in offspring if not ind.fitness.valid]
    fitnesses = map(toolbox.evaluate, invalids)
    for ind, fit in zip(invalids, fitnesses):
        ind.fitness.values = fit
    
    # replace population
    population[:] = offspring

    # stats
    print(f"generation: {gen}")

