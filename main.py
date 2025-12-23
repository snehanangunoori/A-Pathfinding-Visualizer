from grid import Node
from astar import astar
from heuristics import manhattan_distance
from gui import GridGUI

def main():
    rows, cols = 15, 20
    grid = create_grid(rows, cols)
    start = grid[2][2]
    goal = grid[12][17]
    obstacles = [
        (5, 5), (5, 6), (5, 7), (5, 8),
        (6, 8), (7, 8), (8, 8),
        (9, 8), (10, 8)
    ]
    add_obstacles(grid, obstacles)
    
    # Run A* algorithm
    path, explored = astar(start, goal, grid, manhattan_distance)

    # Launch GUI
    gui = GridGUI(grid, start, goal, path, explored)
    gui.run()


def create_grid(rows, cols):
    grid = [[Node(r, c) for c in range(cols)] for r in range(rows)]
    return grid

def add_obstacles(grid, obstacle_positions):
    for r, c in obstacle_positions:
        grid[r][c].walkable = False


if __name__ == "__main__":
    main()
