class MonkeyBananaProblem:
    def __init__(self, initial_state):
        self.state = initial_state

    def actions(self, state):
        # Define possible actions based on the current state
        actions = []
        monkey_position, has_box, box_position, banana_position = state

        if not has_box:
            actions.append("Grab Box")
        else:
            if monkey_position < box_position:
                actions.append("Move Right")
            elif monkey_position > box_position:
                actions.append("Move Left")

            if monkey_position == box_position and monkey_position != banana_position:
                actions.append("Climb Box")

        return actions

    def result(self, state, action):
        # Define the result of taking an action in the current state
        monkey_position, has_box, box_position, banana_position = state

        if action == "Grab Box" and monkey_position == 0 and not has_box:
            return (monkey_position, True, box_position, banana_position)
        elif action == "Move Right" and monkey_position < 4:
            return (monkey_position + 1, has_box, box_position, banana_position)
        elif action == "Move Left" and monkey_position > 0:
            return (monkey_position - 1, has_box, box_position, banana_position)
        elif action == "Climb Box" and monkey_position == box_position:
            return (monkey_position, has_box, box_position, banana_position)

        # If the action is not valid, return the current state
        return state

    def goal_test(self, state):
        # Check if the goal state is reached
        return state == (4, True, 4, 4)

    def is_valid_state(self, state):
        # Check if the state is valid
        monkey_position, has_box, box_position, banana_position = state
        return 0 <= monkey_position <= 4 and 0 <= box_position <= 4 and 0 <= banana_position <= 4

    def solve(self):
        # Solve the problem using a simple search algorithm
        frontier = [(self.state, [])]

        while frontier:
            current_state, actions = frontier.pop(0)

            if self.goal_test(current_state):
                return actions

            for action in self.actions(current_state):
                new_state = self.result(current_state, action)
                if self.is_valid_state(new_state):
                    new_actions = actions + [action]
                    frontier.append((new_state, new_actions))

        return None

# Example usage
if __name__ == "__main__":
    initial_state = (0, False, 0, 0)
    problem = MonkeyBananaProblem(initial_state)
    solution = problem.solve()

    if solution:
        print("Solution:")
        for action in solution:
            print(f"- {action}")
    else:
        print("No solution found.")
