from app.genetic_algorithm import evolve_population
from app.visualization import visualize

def main():
    population = initialize_population()
    for _ in range(GENERATIONS):
        population = evolve_population(population)
        visualize(population)

if __name__ == "__main__":
    main()
