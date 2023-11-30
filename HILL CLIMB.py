import random

def hill_climbing(problem, max_iterations=1000):
    current_solution = problem.initial_solution()
    current_value = problem.evaluate(current_solution)

    for _ in range(max_iterations):
        neighbors = problem.generate_neighbors(current_solution)
        if not neighbors:
            break  # If no neighbors, break the loop

        next_solution = max(neighbors, key=problem.evaluate)
        next_value = problem.evaluate(next_solution)

        if next_value <= current_value:
            break  # If no improvement, break the loop

        current_solution, current_value = next_solution, next_value

    return current_solution, current_value

# Example usage:
class SimpleHillClimbingProblem:
    def _init_(self):
        pass

    def initial_solution(self):
        return random.randint(0, 100)

    def generate_neighbors(self, solution):
        return [solution - 1, solution + 1]

    def evaluate(self, solution):
        # Example objective function: negative of the squared difference from the target value 50
        target_value = 50
        return -(solution - target_value) ** 2

problem = SimpleHillClimbingProblem()
final_solution, final_value = hill_climbing(problem)

print("Final Solution:", final_solution)
print("Final Value:", final_value)
