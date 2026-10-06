edges = [
    (0, 1, 10),
    (0, 2, 6),
    (0, 3, 5),
    (1, 3, 15),
    (2, 3, 4)
]

parent = [0, 1, 2, 3]


def find(x):
    while parent[x] != x:
        x = parent[x]
    return x


def union(x, y):
    root_x = find(x)
    root_y = find(y)

    if root_x != root_y:
        parent[root_y] = root_x
        return True

    return False


edges.sort(key=lambda x: x[2])

total = 0
count = 0

print("Minimum Spanning Tree:")

for u, v, weight in edges:

    if union(u, v):
        print(u, "--", v, "=", weight)
        total += weight
        count += 1

        if count == len(parent) - 1:
            break

print("Total Cost:", total)
