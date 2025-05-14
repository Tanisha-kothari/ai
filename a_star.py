map = {
    'A': {'B': 2, 'C': 3},
    'B': {'D': 2, 'E': 5},
    'C': {'F': 4},
    'D': {},
    'E': {},
    'F': {}
}

# Heuristic (guess) to reach goal
hint = {
    'A': 6,
    'B': 4,
    'C': 4,
    'D': 2,
    'E': 0,
    'F': 0
}


def astar(start, goal):
    todo = [start]         
    cost = {start: 0}      
    from_node = {}        

    while todo:
        now = min(todo, key=lambda x: cost[x] + hint[x])
        g = cost[now]
        h = hint[now]
        f = g + h
        print(f"Exploring node: {now} with f={f}, g={g}, h={h}")

        if now == goal:
            path = [now]
            while now in from_node:
                now = from_node[now]
                path.append(now)
            path.reverse()
            print("Goal found:", goal)
            print("Path:", ' -> '.join(path))
            print("Total Cost:", cost[goal])
            return

        todo.remove(now)

        for next in map[now]:
            new = cost[now] + map[now][next]
            if next not in cost or new < cost[next]:
                cost[next] = new
                from_node[next] = now
                g2 = new
                h2 = hint[next]
                f2 = g2 + h2
                print(f"  Adding child {next} with f={f2}, g={g2}, h={h2}")
                if next not in todo:
                    todo.append(next)

    print("Goal not found.")

astar('A', 'F')
