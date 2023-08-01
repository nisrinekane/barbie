import random
from deap import base, creator, tools

POINT_COUNT = 100 
POPULATION_SIZE = 50 


# define the fitness function
creator.create('FitnessMax', base.Fitness, weights=(1.0,))
creator.create('Inidividual', list, fitness=creator.FitnessMax)

toolbox = base.Toolbox()

# attribute generator
toolbox.register('attr_point', lambda: (random.uniform(0, 1), random.uniform(0, 1)))

# structure initializers
toolbox.register('individual', tools.initRepeat, creator.Individual, toolbox.attr_point, n=POINT_COUNT)
toolbox.register('population', tools.initRepeat, list, toolbox.individual, n=POPULATION_SIZE)

population = toolbox.population()