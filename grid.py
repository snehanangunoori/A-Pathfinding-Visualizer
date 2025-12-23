class Node:
    def __init__(self, row, col, walkable=True):
        self.row = row
        self.col = col
        self.walkable = walkable

    def __eq__(self, other):
        return (self.row, self.col) == (other.row, other.col)

    def __hash__(self):
        return hash((self.row, self.col))
