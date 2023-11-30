class SlidingPuzzle:
    def __init__(self):
        # Initialize the puzzle board
        self.board = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]  # 0 represents the empty space
        self.empty_position = (2, 2)  # Initial position of the empty space

    def display(self):
        # Display the current state of the puzzle
        for row in self.board:
            print(" ".join(map(str, row)))
        print()

    def move(self, direction):
        # Move the empty space in the specified direction
        row, col = self.empty_position
        if direction == 'up' and row > 0:
            self.board[row][col], self.board[row - 1][col] = self.board[row - 1][col], self.board[row][col]
            self.empty_position = (row - 1, col)
        elif direction == 'down' and row < 2:
            self.board[row][col], self.board[row + 1][col] = self.board[row + 1][col], self.board[row][col]
            self.empty_position = (row + 1, col)
        elif direction == 'left' and col > 0:
            self.board[row][col], self.board[row][col - 1] = self.board[row][col - 1], self.board[row][col]
            self.empty_position = (row, col - 1)
        elif direction == 'right' and col < 2:
            self.board[row][col], self.board[row][col + 1] = self.board[row][col + 1], self.board[row][col]
            self.empty_position = (row, col + 1)
        else:
            print("Invalid move!")

    def is_solved(self):
        # Check if the puzzle is in the solved state
        return self.board == [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

# Example usage
puzzle = SlidingPuzzle()
puzzle.display()

while not puzzle.is_solved():
    move_direction = input("Enter move direction (up, down, left, right): ")
    puzzle.move(move_direction)
    puzzle.display()

print("Congratulations! Puzzle solved.")
