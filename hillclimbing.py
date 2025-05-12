import random

# Fitness Function
def fitness(state, target):
    return sum(1 for i in range(len(state)) if state[i] == target[i])

# Generate Neighbors by flipping one bit at a time
def get_neighbors(state):
    neighbors = []
    for i in range(len(state)):
        flipped = '1' if state[i] == '0' else '0'
        neighbor = state[:i] + flipped + state[i+1:]
        neighbors.append(neighbor)
    return neighbors

# Simple Hill Climbing
def simple_hill_climbing(initial, target):
    current = initial
    current_fit = fitness(current, target)
    print(f"Start: {current} (Fitness: {current_fit})")

    while True:
        neighbors = get_neighbors(current)
        for neighbor in neighbors:
            fit = fitness(neighbor, target)
            print(f"Checking neighbor: {neighbor} (Fitness: {fit})")
            if fit > current_fit:
                current = neighbor
                current_fit = fit
                print(f"Moved to: {current} (Fitness: {fit})")
                break
        else:
            print("No better neighbor found. Stuck.")
            break

        if current == target:
            print("Target reached!")
            break

# Steepest Ascent Hill Climbing
def steepest_ascent(initial, target):
    current = initial
    current_fit = fitness(current, target)
    print(f"Start: {current} (Fitness: {current_fit})")

    while True:
        neighbors = get_neighbors(current)
        best_neighbor = current
        best_fit = current_fit

        for neighbor in neighbors:
            fit = fitness(neighbor, target)
            print(f"Neighbor: {neighbor} (Fitness: {fit})")
            if fit > best_fit:
                best_neighbor = neighbor
                best_fit = fit

        if best_fit == current_fit:
            print("No better neighbor found. Stuck.")
            break
        else:
            current = best_neighbor
            current_fit = best_fit
            print(f"Moved to: {current} (Fitness: {current_fit})")

        if current == target:
            print("Target reached!")
            break

# Stochastic Hill Climbing
def stochastic_hill_climbing(initial, target):
    current = initial
    current_fit = fitness(current, target)
    print(f"Start: {current} (Fitness: {current_fit})")

    while True:
        neighbors = get_neighbors(current)
        random.shuffle(neighbors)
        moved = False

        for neighbor in neighbors:
            fit = fitness(neighbor, target)
            print(f"Trying: {neighbor} (Fitness: {fit})")
            if fit > current_fit:
                current = neighbor
                current_fit = fit
                moved = True
                print(f"Moved to: {current} (Fitness: {fit})")
                break

        if not moved:
            print("No better neighbor found. Stuck.")
            break

        if current == target:
            print("Target reached!")
            break

# Main Menu
def main():
    initial = input("Enter initial state (e.g., 0101): ")
    target = input("Enter target state (e.g., 1111): ")

    print("\nChoose Hill Climbing Method:")
    print("1. Simple Hill Climbing")
    print("2. Steepest Ascent Hill Climbing")
    print("3. Stochastic Hill Climbing")

    choice = input("Enter choice (1/2/3): ")

    print("\n--- Execution Trace ---\n")
    if choice == '1':
        simple_hill_climbing(initial, target)
    elif choice == '2':
        steepest_ascent(initial, target)
    elif choice == '3':
        stochastic_hill_climbing(initial, target)
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
