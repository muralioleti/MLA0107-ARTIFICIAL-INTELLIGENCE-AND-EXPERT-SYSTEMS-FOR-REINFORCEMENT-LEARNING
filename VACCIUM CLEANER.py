class VacuumCleaner:
    def __init__(self, grid):
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0])
        self.current_position = (0, 0)

    def is_valid_move(self, move):
        new_position = (self.current_position[0] + move[0], self.current_position[1] + move[1])
        return 0 <= new_position[0] < self.rows and 0 <= new_position[1] < self.cols

    def move(self, direction):
        moves = {
            'up': (-1, 0),
            'down': (1, 0),
            'left': (0, -1),
            'right': (0, 1)
        }
        move = moves.get(direction)
        if move and self.is_valid_move(move):
            self.current_position = (self.current_position[0] + move[0], self.current_position[1] + move[1])

    def clean(self):
        dirty_cells = sum(row.count('D') for row in self.grid)

        while dirty_cells > 0:
            current_cell_status = self.grid[self.current_position[0]][self.current_position[1]]

            if current_cell_status == 'D':
                print(f"Cleaning cell at {self.current_position}")
                self.grid[self.current_position[0]][self.current_position[1]] = 'C'
                dirty_cells -= 1

            # Move to the next cell (minimizing movement)
            if self.current_position[1] < self.cols - 1:
                self.move('right')
            elif self.current_position[0] < self.rows - 1:
                self.move('down')
            elif self.current_position[1] > 0:
                self.move('left')
            elif self.current_position[0] > 0:
                self.move('up')

if __name__ == "__main__":
    # Example grid (C: Clean, D: Dirty)
    grid = [
        ['C', 'D', 'C', 'D', 'C'],
        ['C', 'C', 'D', 'C', 'C'],
        ['D', 'C', 'C', 'D', 'C'],
        ['C', 'C', 'C', 'C', 'D'],
        ['D', 'C', 'C', 'C', 'D']
    ]

    cleaner = VacuumCleaner(grid)
    cleaner.clean()
