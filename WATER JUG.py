def water_jug_problem(jug1_capacity, jug2_capacity, target):
    visited_states = set()
    queue = [(0, 0)]  # Initial state: both jugs are empty

    while queue:
        current_state = queue.pop(0)

        # Check if the target is reached
        if current_state[0] == target:
            return current_state

        # Try all possible operations: fill, empty, pour
        operations = [
            (jug1_capacity, current_state[1]),  # Fill jug1
            (current_state[0], jug2_capacity),  # Fill jug2
            (0, current_state[1]),  # Empty jug1
            (current_state[0], 0),  # Empty jug2
            (min(current_state[0] + current_state[1], jug1_capacity),
             max(0, current_state[0] + current_state[1] - jug1_capacity)),  # Pour from jug2 to jug1
            (max(0, current_state[0] + current_state[1] - jug2_capacity),
             min(current_state[0] + current_state[1], jug2_capacity)),  # Pour from jug1 to jug2
        ]

        for operation in operations:
            if operation not in visited_states:
                visited_states.add(operation)
                queue.append(operation)

    return None  # No solution found

# Example usage
solution = water_jug_problem(jug1_capacity=4, jug2_capacity=3, target=2)

if solution:
    print(f"Solution found: {solution}")
else:
    print("No solution found.")
