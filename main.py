from collections import deque

def shortest_path(rooms, doors, start, goal):
    """
    Compute one shortest path between start and goal in an undirected graph.
    """

    # If no rooms, or rooms missing, or start/goal not real → no path
    if start == goal:
        return [start] if start in rooms else []

    if start not in rooms or goal not in rooms:
        return []

    # Build adjacency list
    graph = {r: [] for r in rooms}
    for a, b in doors:
        graph[a].append(b)
        graph[b].append(a)

    # BFS setup
    queue = deque([start])
    visited = {start}
    parent = {start: None}

    # BFS search
    while queue:
        curr = queue.popleft()

        if curr == goal:
            break

        for neighbor in graph[curr]:
            if neighbor not in visited:
                visited.add(neighbor)
                parent[neighbor] = curr
                queue.append(neighbor)

    # If goal never reached
    if goal not in parent:
        return []

    # Reconstruct path backward
    path = []
    node = goal
    while node is not None:
        path.append(node)
        node = parent[node]

    # Reverse to get start → goal
    path.reverse()
    return path
