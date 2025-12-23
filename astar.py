import heapq
from itertools import count


def get_neighbors(node, grid):
    neighbors = []
    directions = [
        (-1, 0),  # up
        (1, 0),   # down
        (0, -1),  # left
        (0, 1)    # right
    ]

    rows = len(grid)
    cols = len(grid[0])

    for dr, dc in directions:
        r = node.row + dr
        c = node.col + dc

        if 0 <= r < rows and 0 <= c < cols:
            neighbors.append(grid[r][c])

    return neighbors


def astar(start, goal, grid, heuristic):
    
    open_set = []
    counter = count() # for tie-breaking
    heapq.heappush(open_set, (0, next(counter), start))

    g_score = {start: 0}
    parent = {} # To reconstruct path
    visited = set()

    while open_set:
        _, _, current = heapq.heappop(open_set)

        if current == goal:
            return reconstruct_path(parent, current), visited

        visited.add(current)
        
        tentative_g = g_score[current] + 1  # Assuming uniform cost for each edge

        for neighbor in get_neighbors(current, grid):
            if not neighbor.walkable or neighbor in visited:
                continue
            if neighbor not in g_score or tentative_g < g_score[neighbor]:
                parent[neighbor] = current
                g_score[neighbor] = tentative_g
                f = tentative_g + heuristic(neighbor, goal)
                heapq.heappush(open_set, (f, next(counter), neighbor))

    return None, visited


def reconstruct_path(parent, current):
    path = [current]
    while current in parent:
        current = parent[current]
        path.append(current)
    return path[::-1]
