import numpy as np
import math
import random

def objective_function(x):
    # Define your objective function here.
    # This is the function that you want to minimize or maximize.
    return x**2 + 3*x + 5  # Example function, replace with your own.

def acceptance_probability(old_cost, new_cost, temperature):
    if new_cost < old_cost:
        return 1.0
    return math.exp((old_cost - new_cost) / temperature)

def simulated_annealing(initial_solution, temperature, cooling_rate, iterations):
    current_solution = initial_solution
    current_cost = objective_function(current_solution)

    best_solution = current_solution
    best_cost = current_cost

    for iteration in range(iterations):
        temperature *= cooling_rate

        # Generate a neighboring solution
        neighbor_solution = current_solution + np.random.uniform(-0.1, 0.1)
        neighbor_cost = objective_function(neighbor_solution)

        # Accept the new solution with a certain probability
        if acceptance_probability(current_cost, neighbor_cost, temperature) > random.random():
            current_solution = neighbor_solution
            current_cost = neighbor_cost

        # Update the best solution if needed
        if current_cost < best_cost:
            best_solution = current_solution
            best_cost = current_cost

    return best_solution, best_cost

# Example usage
if __name__ == "__main__":
    # Set random seed for reproducibility
    np.random.seed(42)

    # Initial solution
    initial_solution = np.random.uniform(-10, 10)

    # Parameters
    initial_temperature = 100.0
    cooling_rate = 0.95
    iterations = 1000

    # Run simulated annealing
    best_solution, best_cost = simulated_annealing(initial_solution, initial_temperature, cooling_rate, iterations)

    print("Best Solution:", best_solution)
    print("Best Cost:", best_cost)
