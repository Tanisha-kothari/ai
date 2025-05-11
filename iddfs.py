def dls(tree, current, goal, limit, path):
    path.append(current)
    
    if current == goal:
        return True

    if limit <= 0:
        path.pop()
        return False

    for neighbor in tree.get(current, []):
        if dls(tree, neighbor, goal, limit - 1, path):
            return True

    path.pop()
    return False

def iddfs(tree, limit, start, goal):
    for depth in range(limit + 1):
        path = []
        print(f"Trying depth limit: {depth}")
        if dls(tree, start, goal, depth, path):
            return path
    return None
            

tree = {
    'A' : ['B', 'C'],
    'B' : ['D', 'E'],
    'C' : ['F', 'G'],
    'D' : [],
    'E' : [],
    'F' : [],
    'G' : []
}

start = 'A'
goal = 'G'
max_depth = 2

result = iddfs(tree, max_depth, start, goal)

if result:
    print("Path found:", result)
else:
    print("No path found.")
