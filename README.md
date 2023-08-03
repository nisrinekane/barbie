# Genetic Algorithm for Generating "Barbie" text

This project uses a genetic algorithm which is a type of evolutionary computing technique to generate points that form a representation of the word "Barbie" in a 2D space.

An evolutionary algorithm is a method inspired by biological evolution. The algorithm starts with a population of randomly generated "individuals". In the case of this current project, an individual is a set of points in a 2D space. The population evolves over time through a process of selection, crossover and mutation.

The "fitness" of each individual (how close the representation of the word "Barbie" it forms) is measured using a scoring function. The individuals with the highest fitness have a higher chance of passing on their "genes" to the next generation.

Over many generations, the population will evolve to produce better and better approximations of the word "Barbie".

## Project Structure

```
/barbie
    /app
        /genetic_algorithm.py   # is main genetic algorithm.
        /scoring.py             # is scoring function.
        /visualization.py       # is visualization function.
    README.md                   # Project description
```

## Setup


1. Clone this repository to your local machine using `git clone https://github.com/nisrinekane/barbie.git`.

2. (recommended) Create a virtual environment and activate it.

3. Install the required dependencies using `pip install -r requirements.txt`.

4. Run main script  `python src/genetic_algorithm.py`.

## Usage

To run the project navigate to the root directory and execute the following command: `python src/genetic_algorithm.py`.

## Customization

You can customize the behavior of the genetic algorithm by modifying the parameters in `src/genetic_algorithm.py`:

- `POINT_COUNT`: The number of points in each individual.
- `POPULATION_SIZE`: The size of the population.
- `NGEN`: The number of generations to run the genetic algorithm for.

You can also customize the genetic operations by modifying the `evaluate`, `mutate`, and `mate` functions in `src/genetic_algorithm.py`. You'll need to replace the `evaluate` function with a function that calculates how much an individual's shape resembles the word "Barbie".

## Dependencies

This project uses the following dependencies:

- [Python](https://www.python.org/) (>= 3.7)
- [DEAP](https://deap.readthedocs.io/en/master/) (>= 1.3.1)

To install these dependencies, run: `pip install -r requirements.txt`.

