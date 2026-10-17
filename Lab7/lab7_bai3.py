# Bai 3: Ford-Fulkerson dung BFS tim duong tang luong (Edmonds-Karp)
from collections import deque

def _find_path(residual, s, t):
    n = len(residual)
    parent = [-1] * n
    seen = [False] * n
    q = deque([s]); seen[s] = True
    while q:
        u = q.popleft()
        for v in range(n):
            if not seen[v] and residual[u][v] > 0:
                parent[v] = u
                seen[v] = True
                if v == t:
                    return parent
                q.append(v)
    return None

def ford_fulkerson(C, s, t):
    if not C or any(len(row) != len(C) for row in C):
        raise ValueError("C phai la ma tran vuong")
    residual = [row[:] for row in C]
    max_flow = 0
    while True:
        parent = _find_path(residual, s, t)
        if parent is None:
            break
        bottleneck = float("inf")
        v = t
        while v != s:
            u = parent[v]
            bottleneck = min(bottleneck, residual[u][v])
            v = u
        v = t
        while v != s:
            u = parent[v]
            residual[u][v] -= bottleneck
            residual[v][u] += bottleneck
            v = u
        max_flow += bottleneck
    return max_flow, residual

if __name__ == "__main__":
    C = [[0,10,10,0], [0,0,2,8], [0,0,0,9], [0,0,0,0]]
    flow, residual = ford_fulkerson(C, 0, 3)
    print("Max Flow:", flow) # 17
    print("Residual:")
    for row in residual: print(row)
