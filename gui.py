import tkinter as tk

class GridGUI:
    def __init__(self, grid, start, goal, path, explored):
        self.grid = grid
        self.start = start
        self.goal = goal
        self.path = set(path) if path else set()
        self.explored = explored

        self.rows = len(grid)
        self.cols = len(grid[0])
        self.cell_size = 30

        self.root = tk.Tk()
        self.root.title("A* Pathfinding Visualizer")

        self.canvas = tk.Canvas(
            self.root,
            width=self.cols * self.cell_size,
            height=self.rows * self.cell_size
        )
        self.canvas.pack()

        self.draw_grid()

    def draw_grid(self):
        for r in range(self.rows):
            for c in range(self.cols):
                node = self.grid[r][c]
                color = self.get_color(node)

                x1 = c * self.cell_size
                y1 = r * self.cell_size
                x2 = x1 + self.cell_size
                y2 = y1 + self.cell_size

                self.canvas.create_rectangle(
                    x1, y1, x2, y2,
                    fill=color,
                    outline="gray"
                )

    def get_color(self, node):
        if not node.walkable:
            return "black"
        if node == self.start:
            return "green"
        if node == self.goal:
            return "red"
        if node in self.path:
            return "yellow"
        if node in self.explored:
            return "light blue"
        return "white"

    def run(self):
        self.root.mainloop()
