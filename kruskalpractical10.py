def kruskal(vertices, edges):
    edge_count = len(vertices)

    if edge_count == 0:
        print("Minimum Spanning Tree:")
        print("Total Minimum Cost: 0")
        return

    parent = {vertex: vertex for vertex in vertices}

    def find(vertex):
        if parent[vertex] != vertex:
            parent[vertex] = find(parent[vertex])
        return parent[vertex]

    def union(first, second):
        first_root = find(first)
        second_root = find(second)

        if first_root == second_root:
            return False

        parent[second_root] = first_root
        return True

    mst = []
    cost = 0
    edges.sort(key=lambda edge: edge[2])

    for start, end, weight in edges:
        if start not in parent or end not in parent:
            continue

        if union(start, end):
            mst.append((start, end, weight))
            cost += weight

        if len(mst) == edge_count - 1:
            break

    if len(mst) != edge_count - 1:
        print("Graph is not connected!")
        return

    print("Minimum Spanning Tree:")
    for start, end, weight in mst:
        print(start, "-", end, ":", weight)

    print("Total Minimum Cost:", cost)


vertices = list(map(int, input("Enter vertices: ").split()))
e = int(input("Enter number of edges: "))

edges = []
print("Enter edges as: source destination weight")

for _ in range(e):
    start, end, weight = map(int, input().split())
    edges.append((start, end, weight))

kruskal(vertices, edges)