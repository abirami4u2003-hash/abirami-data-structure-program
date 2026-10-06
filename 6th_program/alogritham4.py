edges = []

vertices = int(input("Enter number of vertices: "))
number_of_edges = int(input("Enter number of edges: "))

for i in range(number_of_edges):
    print("Enter edge", i + 1)

    u = int(input("Source: "))
    v = int(input("Destination: "))
    w = int(input("Weight: "))

    edges.append((w, u, v))


def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])

    return parent[x]


def kruskal():
    parent = list(range(vertices))

    edges.sort()

    total = 0
    count = 0

    print("\nEdges in MST:")

    for weight, u, v in edges:

        root_u = find(parent, u)
        root_v = find(parent, v)

        if root_u != root_v:
            print(u, "--", v, "=", weight)

            parent[root_v] = root_u

            total += weight
            count += 1

            if count == vertices - 1:
                break

    if count == vertices - 1:
        print("Minimum Cost:", total)
    else:
        print("Graph is disconnected.")


kruskal()
