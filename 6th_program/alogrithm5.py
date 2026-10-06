import heapq

graph = {
    0: [(1, 10), (2, 6), (3, 5)],
    1: [(0, 10), (3, 15)],
    2: [(0, 6), (3, 4)],
    3: [(0, 5), (1, 15), (2, 4)]
}

visited = set()
heap = [(0, 0, -1)]

total = 0

print("Minimum Spanning Tree:")

while heap:
    weight, vertex, parent = heapq.heappop(heap)

    if vertex in visited:
        continue

    visited.add(vertex)

    if parent != -1:
        print(parent, "--", vertex, "=", weight)
        total += weight

    for neighbour, edge_weight in graph[vertex]:
        if neighbour not in visited:
            heapq.heappush(
                heap,
                (edge_weight, neighbour, vertex)
            )

print("Total Cost:", total)
