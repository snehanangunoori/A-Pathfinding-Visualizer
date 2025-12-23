from grid import Node
from astar import astar
from heuristics import manhattan_distance

def test_simple_path():
    grid = [[Node(r, c) for c in range(3)] for r in range(3)]
    start = grid[0][0]
    goal = grid[2][2]

    path, _ = astar(start, goal, grid, manhattan_distance)
    assert len(path) == 5
