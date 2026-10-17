# Bai 2: Kiem tra do thi hai phia bang BFS to 2 mau
from collections import deque

def is_bipartite_bfs(adj_list, num_nodes):
    color = {}
    for start in range(num_nodes):
        if start in color:
            continue
        color[start] = 0
        q = deque([start])
        while q:
            u = q.popleft()
            for v in adj_list.get(u, []):
                if v not in color:
                    color[v] = 1 - color[u]
                    q.append(v)
                elif color[v] == color[u]:
                    return False
    return True

if __name__ == "__main__":
    g_even = {0:[1,3], 1:[0,2], 2:[1,3], 3:[0,2]}
    g_odd = {0:[1,2], 1:[0,2], 2:[0,1]}
    print("Chu trinh 4 dinh:", is_bipartite_bfs(g_even, 4)) # True
    print("Tam giac:", is_bipartite_bfs(g_odd, 3)) # False
