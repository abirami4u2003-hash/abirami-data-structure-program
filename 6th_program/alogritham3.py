class MST:
    def __init__(self, vertices):
        self.vertices = vertices
        self.edges = []

    def add_edge(self, u, v, weight):
        self.edges.append([weight, u, v])

    def find(self, parent, vertex):
        if parent[vertex] != vertex:
            parent[vertex] = self.find(
                parent,
                parent[vertex]
            )

        return parent[vertex]

    def kruskal(self):
        self.edges.sort()

        parent = list(range(self.vertices))

        result = []
        total = 0

        for weight, u, v in self.edges:

            root_u = self.find(parent, u)
            root_v = self.find(parent, v)

            if root_u != root_v:
                result.append((u, v, weight))
                total += weight

                parent[root_v] = root_u

        print("Minimum Spanning Tree:")

        for u, v, weight in result:
            print(u, "--", v, "=", weight)

        print("Total Cost:", total)


g = MST(6)

g.add_edge(0, 1, 4)
g.add_edge(0, 2, 3)
g.add_edge(1, 2, 1)
g.add_edge(1, 3, 2)
g.add_edge(2, 3, 4)
g.add_edge(3, 4, 2)
g.add_edge(4, 5, 6)

g.kruskal()
