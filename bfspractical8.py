#practical 8
#bfs
from collections import deque

def bfs(adj):
    n = len(adj)
    visited = [False] * n
    res = []

    src = 0
    g = deque()

    g.append(src)
    visited[src] = True
    while g:
        u = g.popleft()
        res.append(u)

        for v in adj[u]:
            if not visited[v]:
                g.append(v)
                visited[v] = True

    return res

adj = [
    [1, 2],
    [0, 3],
    [0, 3],
    [1, 2, 4],
    [3]
]

print("BFS Traversal:", bfs(adj))