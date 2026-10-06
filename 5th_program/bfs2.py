graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}


def dfs(start):
    visited = []
    stack = [start]

    while stack:
        vertex = stack.pop()

        if vertex not in visited:
            print(vertex, end=" ")
            visited.append(vertex)

            # Reverse to maintain left-to-right traversal
            for neighbour in reversed(graph[vertex]):
                if neighbour not in visited:
                    stack.append(neighbour)


print("DFS Traversal:")
dfs('A')
