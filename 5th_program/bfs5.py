graph = {
    0: [1],
    1: [0, 2],
    2: [1],
    3: [4],
    4: [3],
    5: []
}


def dfs(vertex, visited):
    visited.add(vertex)

    for neighbour in graph[vertex]:
        if neighbour not in visited:
            dfs(neighbour, visited)


visited = set()
components = 0

for vertex in graph:
    if vertex not in visited:
        components += 1
        dfs(vertex, visited)


print("Number of Connected Components:", components)
