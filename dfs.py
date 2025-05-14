# Example graph: Each node points to its neighbors
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

def dfs(start, visited_nodes):
    # Visit the current node
    print(start)

    # Mark the node as visited
    visited_nodes.append(start)

    # Visit all neighbors of the current node
    for neighbour in graph[start]:
        if neighbour not in visited_nodes:
            dfs(neighbour, visited_nodes)

# Start DFS from node 'A'
visited_nodes = []   # To keep track of visited nodes
dfs('A', visited_nodes)
