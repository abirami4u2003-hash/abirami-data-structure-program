graph = [
    [0, 4, 0, 0, 0, 2],
    [4, 0, 6, 5, 0, 0],
    [0, 6, 0, 3, 1, 0],
    [0, 5, 3, 0, 2, 0],
    [0, 0, 1, 2, 0, 4],
    [2, 0, 0, 0, 4, 0]
]

n = len(graph)
selected = [False] * n
selected[0] = True

mst = []
cost = 0

for _ in range(n - 1):
    minimum = float('inf')
    source = destination = -1

    for i in range(n):
        if selected[i]:
            for j in range(n):
                if graph[i][j] != 0 and not selected[j]:
                    if graph[i][j] < minimum:
                        minimum = graph[i][j]
                        source = i
                        destination = j

    selected[destination] = True
    mst.append((source, destination, minimum))
    cost += minimum

print("Minimum Spanning Tree:")

for u, v, weight in mst:
    print(u, "--", v, ":", weight)

print("Total Cost:", cost)
