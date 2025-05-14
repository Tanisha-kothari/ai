# BFS uses a queue (First In First Out)

# Example graph: Each node points to its neighbors
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

def bfs(start):
    visited_nodes = []      # List to keep track of visited nodes
    queue = []              # Queue to keep track of nodes to visit

    visited_nodes.append(start)   # Mark the start node as visited
    queue.append(start)           # Add start node to queue

    while queue:                 # Run until queue is empty
        current_node = queue.pop(0)  # Get the first node from queue
        print(current_node)          # Visit the node (print it)

        # Get all neighbours of current_node
        for neighbour in graph[current_node]:
            if neighbour not in visited_nodes:
                visited_nodes.append(neighbour)  # Mark as visited
                queue.append(neighbour)          # Add to queue to visit later

# Call BFS starting from node 'A'
bfs('A')
