import random

# Define fitness function
def fitness(chromosome):
    # The fitness function calculates the fitness of a chromosome (solution).
    # In this example, we want to maximize the sum of the values in the chromosome.
    return sum(chromosome)

# Define the genetic algorithm function
def genetic_algorithm(population_size, chromosome_length, generations):
    # Initialize population
    population = []
    for i in range(population_size):
        chromosome = [random.randint(0, 1) for j in range(chromosome_length)]
        population.append(chromosome)

    # Iterate through generations
    for generation in range(generations):
        # Evaluate fitness of each chromosome
        fitness_scores = [(chromosome, fitness(chromosome)) for chromosome in population]

        # Sort population by fitness
        fitness_scores.sort(key=lambda x: x[1], reverse=True)

        # Print the best fitness score for the current generation
        print("Generation {}: Best Fitness Score = {}".format(generation, fitness_scores[0][1]))

        # Create a new population by selecting the fittest chromosomes and breeding them
        new_population = []
        for i in range(population_size):
            # Select two parents from the top half of the population
            parents = random.choices(fitness_scores[:population_size // 2], k=2)

            # Perform crossover to create a new child chromosome
            crossover_point = random.randint(1, chromosome_length - 1)
            child = parents[0][0][:crossover_point] + parents[1][0][crossover_point:]

            # Perform mutation to introduce some randomness
            mutation_prob = 0.1
            for j in range(chromosome_length):
                if random.random() < mutation_prob:
                    child[j] = 1 - child[j]

            # Add child to new population
            new_population.append(child)

        # Update population
        population = new_population

    # Return the fittest chromosome from the final generation
    return fitness_scores[0][0]

# Example usage of the genetic algorithm function
population_size = 50
chromosome_length = 10
generations = 10
fittest_chromosome = genetic_algorithm(population_size, chromosome_length, generations)
print("Fittest Chromosome = {}".format(fittest_chromosome))