class Node:
    def __init__(self, name, parent=None):
        self.name = name
        self.parent = parent
        self.g = 0  # Cost from start to this node
        self.h = 0  # Heuristic to goal
        self.f = 0  # Total cost f = g + h

def reconstruct_path(node):
    path = []
    while node is not None:
        path.append(node.name)
        node = node.parent
    path.reverse()
    return path

def a_star_tree(tree, heuristics, start, goal):
    open_list = []

    # Starting node
    start_node = Node(start)
    start_node.g = 0
    start_node.h = heuristics[start]
    start_node.f = start_node.g + start_node.h
    open_list.append(start_node)

    print(f"Starting node: {start_node.name} with f={start_node.f}, g={start_node.g}, h={start_node.h}")

    while open_list:
        # Get node with lowest f
        current = open_list[0]
        for node in open_list:
            if node.f < current.f:
                current = node

        print(f"\nExploring node: {current.name} with f={current.f}, g={current.g}, h={current.h}")

        if current.name == goal:
            print(f"Goal node {current.name} reached.")
            return reconstruct_path(current)

        open_list.remove(current)

        # Explore children (since it's a tree, no need to track visited)
        for child_name, cost in tree.get(current.name, []):
            child_node = Node(child_name, current)
            child_node.g = current.g + cost
            child_node.h = heuristics[child_name]
            child_node.f = child_node.g + child_node.h

            print(f"  Adding child {child_name} with f={child_node.f}, g={child_node.g}, h={child_node.h}")

            open_list.append(child_node)

    return None


tree = {
    'A': [('B', 2), ('C', 3)],
    'B': [('D', 4), ('E', 1)],
    'C': [('F', 5)],
    'D': [],
    'E': [('G', 2)],
    'F': [],
    'G': []
}

heuristics = {
    'A': 6,
    'B': 4,
    'C': 4,
    'D': 3,
    'E': 2,
    'F': 3,
    'G': 0
}

start = 'A'
goal = 'G'

path = a_star_tree(tree, heuristics, start, goal)

if path:
    print("\nPath found:", path)
else:
    print("\nNo path found.")
