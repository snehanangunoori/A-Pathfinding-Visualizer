from grid import Node
from heuristics import manhattan_distance

def test_manhattan_distance():
    a = Node(0, 0)
    b = Node(3, 4)
    assert manhattan_distance(a, b) == 7
