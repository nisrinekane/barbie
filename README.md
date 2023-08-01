# Genetic Algorithm for Generating "Barbie" text

This project uses a genetic algorithm to generate points that form a representation of the word "Barbie" in a 2D space. 

## Project Structure

This project is structured as follows:

```
/barbie-genetic-algorithm
    /src
        /genetic_algorithm.py   # is main genetic algorithm.
        /scoring.py             # is scoring function.
        /visualization.py       # is visualization function.
    README.md                   # Project description
```

## Setup

You can set up and run this project as follows:

1. Clone this repository to your local machine using `git clone https://github.com/nisrinekane/barbie.git`.

2. (Optional) Create a virtual environment and activate it.

3. Install the required dependencies using `pip install -r requirements.txt`.

4. Run the main script using `python src/genetic_algorithm.py`.

## Usage

This project uses a simple genetic algorithm to evolve a population of individuals, where each individual is a list of 2D points. 

The goal is to evolve this population over time such that it forms an image resembling the word "Barbie".

To run the project, navigate to the root directory and execute the following command: `python src/genetic_algorithm.py`.

## Customization

You can customize the behavior of the genetic algorithm by modifying the parameters in `src/genetic_algorithm.py`:

- `POINT_COUNT`: The number of points in each individual.
- `POPULATION_SIZE`: The size of the population.
- `NGEN`: The number of generations to run the genetic algorithm for.

You can also customize the genetic operations by modifying the `evaluate`, `mutate`, and `mate` functions in `src/genetic_algorithm.py`. Note that you'll need to replace the `evaluate` function with a function that calculates how much an individual's shape resembles the word "Barbie".

## Dependencies

This project uses the following dependencies:

- [Python](https://www.python.org/) (>= 3.7)
- [DEAP](https://deap.readthedocs.io/en/master/) (>= 1.3.1)

To install these dependencies, run: `pip install -r requirements.txt`.

