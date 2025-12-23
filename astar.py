import heapq

def astar(start, goal, grid, heuristic):
    """
    TODO:
    Implement A* search

    Returns:
    - path: list of nodes from start to goal
    - explored: set of visited nodes
    """

    open_set = []
    heapq.heappush(open_set, (0, start))

    g_score = {start: 0}
    parent = {}
    explored = set()

    while open_set:
        _, current = heapq.heappop(open_set)

        if current == goal:
            return reconstruct_path(parent, current), explored

        explored.add(current)

        for neighbor in get_neighbors(current, grid):
            if not neighbor.walkable or neighbor in explored:
                continue

            tentative_g = g_score[current] + 1

            if neighbor not in g_score or tentative_g < g_score[neighbor]:
                parent[neighbor] = current
                g_score[neighbor] = tentative_g
                f = tentative_g + heuristic(neighbor, goal)
                heapq.heappush(open_set, (f, neighbor))

    return None, explored


def reconstruct_path(parent, current):
    path = [current]
    while current in parent:
        current = parent[current]
        path.append(current)
    return path[::-1]
