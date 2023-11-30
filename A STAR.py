import heapq

class Node:
    def __init__(self, row, col, cost=0, heuristic=0):
        self.row = row
        self.col = col
        self.cost = cost
        self.heuristic = heuristic
        self.total_cost = cost + heuristic
        self.parent = None

    def __lt__(self, other):
        return self.total_cost < other.total_cost

def heuristic(node, goal):
    # Euclidean distance heuristic
    return ((node.row - goal.row) ** 2 + (node.col - goal.col) ** 2) ** 0.5

def astar(grid, start, goal):
    rows, cols = len(grid), len(grid[0])
    visited = set()

    priority_queue = []
    heapq.heappush(priority_queue, start)

    while priority_queue:
        current_node = heapq.heappop(priority_queue)

        if (current_node.row, current_node.col) == (goal.row, goal.col):
            path = []
            while current_node:
                path.append((current_node.row, current_node.col))
                current_node = current_node.parent
            return path[::-1]

        if (current_node.row, current_node.col) in visited:
            continue

        visited.add((current_node.row, current_node.col))

        neighbors = [
            (current_node.row - 1, current_node.col),
            (current_node.row + 1, current_node.col),
            (current_node.row, current_node.col - 1),
            (current_node.row, current_node.col + 1),
        ]

        for neighbor_row, neighbor_col in neighbors:
            if 0 <= neighbor_row < rows and 0 <= neighbor_col < cols and grid[neighbor_row][neighbor_col] != 1:
                neighbor_node = Node(
                    neighbor_row,
                    neighbor_col,
                    cost=current_node.cost + 1,
                    heuristic=heuristic(Node(neighbor_row, neighbor_col), goal)
                )
                neighbor_node.parent = current_node
                heapq.heappush(priority_queue, neighbor_node)

    return None

# Example Usage:
grid = [
    [0, 0, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 0, 0],
]

start_node = Node(0, 0)
goal_node = Node(4, 4)

result = astar(grid, start_node, goal_node)

if result:
    print("Path found:", result)
else:
    print("No path found.")
