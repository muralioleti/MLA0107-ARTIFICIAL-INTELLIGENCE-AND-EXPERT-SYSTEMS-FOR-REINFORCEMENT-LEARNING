import sys

def nearest_neighbor(graph):
    num_cities = len(graph)
    unvisited = set(range(1, num_cities))
    current_city = 0  # Starting from the first city
    tour = [current_city]

    while unvisited:
        nearest_city = min(unvisited, key=lambda city: graph[current_city][city])
        tour.append(nearest_city)
        unvisited.remove(nearest_city)
        current_city = nearest_city

    # Return to the starting city
    tour.append(tour[0])

    return tour

def total_distance(tour, graph):
    total = 0
    for i in range(len(tour) - 1):
        total += graph[tour[i]][tour[i + 1]]
    return total

# Example usage
if __name__ == "__main__":
    # Example graph (distance matrix)
    graph = [
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0]
    ]

    # Find the tour using the nearest neighbor algorithm
    tour = nearest_neighbor(graph)

    # Print the tour and its total distance
    print("Tour:", tour)
    print("Total Distance:", total_distance(tour, graph))
