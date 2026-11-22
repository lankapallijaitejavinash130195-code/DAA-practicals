from itertools import product


def floyd_warshall(graph):
    n = len(graph)
    dist = [row[:] for row in graph]
    for k in range(n):
        for i, j in product(range(n), repeat=2):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    return dist

INF = float("inf")
adj_matrix = [
    [0, 3, 10, INF],
    [INF, 0, 1, 7],
    [INF, INF, 0, 2],
    [INF, INF, INF, 0],
]
shortest_paths = floyd_warshall(adj_matrix)
print(shortest_paths)