from collections import deque

graph = {
    0: [1, 2],
    1: [0, 3],
    2: [0],
    3: [1],
    4: [5],
    5: [4]
}


def bfs(start, visited):
    queue = deque([start])
    visited.add(start)

    while queue:
        vertex = queue.popleft()
        print(vertex, end=" ")

        for neighbour in graph[vertex]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)


visited = set()

print("BFS of Disconnected Graph:")

for vertex in graph:
    if vertex not in visited:
        bfs(vertex, visited)
