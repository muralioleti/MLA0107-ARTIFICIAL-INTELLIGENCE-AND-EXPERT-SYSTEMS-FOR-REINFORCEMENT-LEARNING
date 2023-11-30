class State:
    def __init__(self, missionaries, cannibals, boat, parent=None):
        self.missionaries = missionaries
        self.cannibals = cannibals
        self.boat = boat
        self.parent = parent

    def is_valid(self):
        # Check if the state is valid
        if (self.missionaries < 0 or self.cannibals < 0 or
                self.missionaries > 3 or self.cannibals > 3):
            return False
        # Check if missionaries are eaten
        if (self.cannibals > self.missionaries > 0 or
                self.cannibals < self.missionaries < 3):
            return False
        return True

    def is_goal(self):
        # Check if the goal is reached
        return self.missionaries == 0 and self.cannibals == 0 and self.boat == 0

    def __str__(self):
        return f'M({self.missionaries}) C({self.cannibals}) B({self.boat})'

def get_valid_moves(state):
    moves = []
    if state.boat == 0:  # Boat on the left side
        for m in range(3):
            for c in range(3):
                if 0 < m + c <= 2:
                    moves.append((m, c))
    else:  # Boat on the right side
        for m in range(-2, 1):
            for c in range(-2, 1):
                if 0 < -m - c <= 2:
                    moves.append((m, c))
    return moves

def apply_move(state, move):
    new_state = State(state.missionaries + move[0],
                      state.cannibals + move[1],
                      1 - state.boat,
                      state)
    return new_state

def print_solution(solution):
    path = []
    while solution:
        path.append(solution)
        solution = solution.parent

    for t in path[::-1]:
        print(t)

def solve():
    initial_state = State(3, 3, 1)
    frontier = [initial_state]
    explored = set()

    while frontier:
        state = frontier.pop(0)

        if state.is_goal():
            print_solution(state)
            return

        explored.add((state.missionaries, state.cannibals, state.boat))

        for move in get_valid_moves(state):
            new_state = apply_move(state, move)

            if new_state.is_valid() and (new_state.missionaries, new_state.cannibals, new_state.boat) not in explored:
                frontier.append(new_state)

    print("No solution found.")

if __name__ == "__main__":
    solve()
