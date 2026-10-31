from collections import deque

# Same undirected graph is represented in two forms.
vertices = ["A", "B", "C", "D", "E"]

# Adjacency list for BFS
adj_list = {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A", "E"],
    "D": ["B"],
    "E": ["B", "C"]
}

# Adjacency matrix for DFS (vertex order: A, B, C, D, E)
adj_matrix = [
    [0, 1, 1, 0, 0],  # A
    [1, 0, 0, 1, 1],  # B
    [1, 0, 0, 0, 1],  # C
    [0, 1, 0, 0, 0],  # D
    [0, 1, 1, 0, 0]   # E
]


def bfs(start):
    visited = set([start])
    queue = deque([start])
    order = []

    while queue:
        vertex = queue.popleft()
        order.append(vertex)

        for neighbour in adj_list[vertex]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)

    return order


def dfs(start):
    start_index = vertices.index(start)
    visited = set()
    order = []

    def visit(vertex_index):
        visited.add(vertex_index)
        order.append(vertices[vertex_index])

        for neighbour_index in range(len(vertices)):
            if (adj_matrix[vertex_index][neighbour_index] == 1
                    and neighbour_index not in visited):
                visit(neighbour_index)

    visit(start_index)
    return order


start = input("Enter starting location (A-E): ").upper()

if start in vertices:
    print("BFS Traversal:", bfs(start))
    print("DFS Traversal:", dfs(start))
else:
    print("Invalid starting location.")
