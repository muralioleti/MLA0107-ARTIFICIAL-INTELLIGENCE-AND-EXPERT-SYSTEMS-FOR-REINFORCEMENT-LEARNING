from queue import PriorityQueue

def best_first_search(graph, start, goal, heuristic):
    visited = set()
    priority_queue = PriorityQueue()
    priority_queue.put((heuristic(start, goal), start))

    while not priority_queue.empty():
        current_node = priority_queue.get()[1]

        if current_node == goal:
            print("Goal reached!")
            return True

        if current_node not in visited:
            print("Visiting node:", current_node)
            visited.add(current_node)

            for neighbor, cost in graph[current_node]:
                if neighbor not in visited:
                    priority_queue.put((heuristic(neighbor, goal), neighbor))

    print("Goal not reached.")
    return False

# Example usage
if __name__ == "__main__":
    # Example graph represented as an adjacency list
    graph = {
        'A': [('B', 5), ('C', 3)],
        'B': [('D', 7)],
        'C': [('E', 8)],
        'D': [('F', 2)],
        'E': [],
        'F': []
    }

    start_node = 'A'
    goal_node = 'F'

    # Example heuristic function (distance from the current node to the goal)
    def heuristic(node, goal):
        heuristic_values = {'A': 10, 'B': 7, 'C': 5, 'D': 3, 'E': 2, 'F': 0}
        return heuristic_values[node]

    # Run Best-First Search
    best_first_search(graph, start_node, goal_node, heuristic)
