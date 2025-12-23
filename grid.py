# Represents a single cell in the grid
class Node:
    def __init__(self, row, col, walkable=True):
        """
        Initialize a grid node.
        
        Args:
            row (int): The row position of the node in the grid
            col (int): The column position of the node in the grid
            walkable (bool): Whether this node can be traversed or is an obstacle (default: True)
        """
        self.row = row
        self.col = col
        self.walkable = walkable

    def __eq__(self, other):
        return (self.row, self.col) == (other.row, other.col)

    def __hash__(self):
        return hash((self.row, self.col))
