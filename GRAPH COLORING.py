class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = {vertex: [] for vertex in range(vertices)}

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def greedy_coloring(self):
        colors = [-1] * self.vertices
        available_colors = set(range(self.vertices))

        for vertex in range(self.vertices):
            for neighbor in self.graph[vertex]:
                if colors[neighbor] != -1:
                    available_colors.discard(colors[neighbor])

            if available_colors:
                color = min(available_colors)
                colors[vertex] = color
                available_colors.add(color)
            else:
                print("Graph cannot be colored with fewer than {} colors.".format(self.vertices))
                return None

            available_colors = set(range(self.vertices))

        return colors

def print_colored_map(graph, colors):
    color_mapping = {0: 'Red', 1: 'Blue', 2: 'Green', 3: 'Yellow', 4: 'Purple', 5: 'Orange', 6: 'Pink'}

    for vertex, color in enumerate(colors):
        print("Region {}: {}".format(vertex, color_mapping[color]))

if __name__ == "__main__":
    # Example usage:
    num_vertices = 5
    g = Graph(num_vertices)

    # Add edges between regions
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 3)
    g.add_edge(2, 4)

    # Greedy coloring
    colors = g.greedy_coloring()

    if colors is not None:
        print_colored_map(g, colors)
