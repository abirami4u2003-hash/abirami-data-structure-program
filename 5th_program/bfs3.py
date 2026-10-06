vertices = 5
graph = [[] for _ in range(vertices)]


def add_edge(u, v):
    graph[u].append(v)
    graph[v].append(u)


add_edge(0, 1)
add_edge(0, 2)
add_edge(1, 3)
add_edge(2, 4)
add_edge(3, 4)


print("Adjacency List:")

for i in range(vertices):
    print(i, "->", graph[i])
