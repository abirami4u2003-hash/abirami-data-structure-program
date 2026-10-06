graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}


def bfs(start):
    visited = []
    queue = [start]

    while queue:
        vertex = queue.pop(0)

        if vertex not in visited:
            print(vertex, end=" ")
            visited.append(vertex)

            for neighbour in graph[vertex]:
                if neighbour not in visited:
                    queue.append(neighbour)


print("BFS Traversal:")
bfs('A')
