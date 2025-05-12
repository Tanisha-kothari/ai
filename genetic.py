import random

# Step 1 : Initial Population
pop_size = int(input("Enter the initial population size : "))
print("Population size : ", pop_size)

initial_pop = []
for i in range(0, pop_size):
    individual = input(f"Enter individual {i+1} : ")
    initial_pop.append(individual)

print('Initial population is as follows : ', initial_pop)

print("What offspring/target? Please enter : ")
target = input()

# Step 2 : Fitness Function
fit_check = {}

for possible_parent in initial_pop:
    fit_check[possible_parent] = 0
    for i in range(len(target)):
        if possible_parent[i] == target[i]:
            fit_check[possible_parent] += 1

print("Fitness function applied. The fitness of each individual is as follows : ")
print(fit_check)

# Step 3 : Selection (select top 2 by fitness)
sorted_fit = sorted(fit_check.items(), key=lambda x: x[1], reverse=True)

parent1 = sorted_fit[0][0]
parent2 = sorted_fit[1][0]

print(f"Selected parents are as follows : {parent1} as parent 1 and {parent2} as parent 2")

# Step 4 : Crossover
point = random.randint(1, len(parent1)-1)
child = parent1[:point] + parent2[point:]

print(f"Crossover point is at index {point}")
print("Here is the generated child : ", child)

# Step 5 : Mutation
MUTATION_RATE = 0.1

mutated_child = ""

for i in range(len(child)):
    if random.random() < MUTATION_RATE:
        # Flip the bit
        if child[i] == "0":
            mutated_child += "1"
        else:
            mutated_child += "0"
    else:
        mutated_child += child[i]

print("After mutation, the child becomes : ", mutated_child)

# Step 6 : Termination Check
if mutated_child == target:
    print("Target offspring has been successfully created. Termination condition.")
else:
    print("Target not reached yet. Try next generation manually or repeat steps in loop.")
