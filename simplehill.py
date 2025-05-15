# Calculate how many bits match between current state and target
def fitness(state, target):
    score = 0
    for i in range(len(state)):
        if state[i] == target[i]:
            score += 1
    return score

# Generate neighbors by flipping one bit at a time
def get_neighbors(state):
    neighbors = []
    for i in range(len(state)):
        if state[i] == '0':
            flipped = '1'
        else:
            flipped = '0'
        neighbor = state[:i] + flipped + state[i+1:]
        neighbors.append(neighbor)
    return neighbors

# Simple Hill Climbing algorithm
def simple_hill_climbing(initial, target):
    current = initial
    while True:
        current_fit = fitness(current, target)
        print(f"Current state: {current}, Fitness: {current_fit}")

        neighbors = get_neighbors(current)

        moved = False  # Track if we move to better neighbor

        for neighbor in neighbors:
            neighbor_fit = fitness(neighbor, target)
            print(f"Checking neighbor: {neighbor}, Fitness: {neighbor_fit}")

            # If neighbor is better, move to it
            if neighbor_fit > current_fit:
                current = neighbor
                moved = True
                print(f"Moved to better state: {current}\n")
                break  # Move as soon as better neighbor is found

        if not moved:
            print("No better neighbor found. Algorithm stopped.")
            break

        if current == target:
            print("Target state reached!")
            break

# Main program starts here
def main():
    initial = input("Enter initial state (like 0101): ")
    target = input("Enter target state (like 1111): ")

    simple_hill_climbing(initial, target)

if __name__ == "__main__":
    main()
