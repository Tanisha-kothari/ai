import random

# Function to calculate fitness (how close is individual to target)
def fitness(individual, target):
    score = 0
    for i in range(len(target)):
        if individual[i] == target[i]:
            score += 1
    return score

# Function to mutate an individual (randomly change characters)
def mutate(individual, mutation_rate, valid_chars):
    new_individual = ""
    for char in individual:
        if random.random() < mutation_rate:
            new_individual += random.choice(valid_chars)
        else:
            new_individual += char
    return new_individual

# Function to crossover two parents and create a child
def crossover(parent1, parent2):
    point = random.randint(1, len(parent1)-1)
    child = parent1[:point] + parent2[point:]
    return child

# Main Genetic Algorithm Function
def genetic_algorithm(target, population_size, mutation_rate, max_generations=1000):
    valid_chars = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 !@#$%^&*()-_=+[]{};:'\",.<>?/|\\")
    
    # Create initial population (random strings of same length as target)
    population = []
    for _ in range(population_size):
        individual = ''.join(random.choice(valid_chars) for _ in range(len(target)))
        population.append(individual)

    generation = 0

    # Loop until target is found or generation limit reached
    while generation < max_generations:
        # Calculate fitness for each individual
        fitness_scores = {}
        for individual in population:
            fitness_scores[individual] = fitness(individual, target)
        
        # Check if target is found
        if target in fitness_scores:
            print(f"Target found in generation {generation}: {target}")
            return
        
        # Select best 2 individuals as parents
        sorted_individuals = sorted(fitness_scores.items(), key=lambda x: x[1], reverse=True)
        parent1 = sorted_individuals[0][0]
        parent2 = sorted_individuals[1][0]

        # Show best of current generation
        print(f"Generation {generation} | Best: {parent1} | Fitness: {fitness_scores[parent1]}")

        # Create new population with crossover and mutation
        new_population = []
        for _ in range(population_size):
            child = crossover(parent1, parent2)
            child = mutate(child, mutation_rate, valid_chars)
            new_population.append(child)

        # Update population and go to next generation
        population = new_population
        generation += 1

    print("Target not found within generation limit.")

# User inputs
target = input("Enter the target string: ")
population_size = int(input("Enter population size: "))
mutation_rate = float(input("Enter mutation rate (between 0 and 1): "))

# Run genetic algorithm
genetic_algorithm(target, population_size, mutation_rate)
