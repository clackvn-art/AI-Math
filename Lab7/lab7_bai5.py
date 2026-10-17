# Bai 5: PageRank va Min-Cut
from lab7_bai3 import ford_fulkerson

def compute_pagerank(P_web, damping_factor=0.85, max_iter=100, tolerance=1e-12):
    n = len(P_web)
    if n == 0 or any(len(row) != n for row in P_web):
        raise ValueError("P_web phai la ma tran vuong")
    rank = [1/n] * n
    for _ in range(max_iter):
        nxt = [(1-damping_factor)/n] * n
        for i in range(n):
            for j in range(n):
                nxt[j] += damping_factor * rank[i] * P_web[i][j]
        if max(abs(nxt[i]-rank[i]) for i in range(n)) < tolerance:
            rank = nxt
            break
        rank = nxt
    total = sum(rank)
    return [x/total for x in rank]

def find_min_cut(C, source, sink):
    max_flow, residual = ford_fulkerson(C, source, sink)
    n = len(C)
    seen = [False]*n
    stack = [source]; seen[source] = True
    while stack:
        u = stack.pop()
        for v in range(n):
            if residual[u][v] > 0 and not seen[v]:
                seen[v] = True
                stack.append(v)
    S = [i for i in range(n) if seen[i]]
    T = [i for i in range(n) if not seen[i]]
    edges = [(u,v,C[u][v]) for u in S for v in T if C[u][v] > 0]
    return max_flow, S, T, edges, sum(c for _,_,c in edges)

if __name__ == "__main__":
    names = ["A","B","C","D"]
    P_web = [[0,.5,.5,0], [0,0,1,0], [1,0,0,0], [0,.5,.5,0]]
    ranks = compute_pagerank(P_web)
    print("PageRank:")
    for name, score in zip(names, ranks): print(f"Server {name}: {score:.4f}")
    # PDF khong cho ma tran dung luong cho Min-Cut, nen dung du lieu minh hoa:
    C = [[0,8,5,0], [0,0,3,6], [0,0,0,7], [0,0,0,0]]
    flow, S, T, cut_edges, cut_cap = find_min_cut(C, 0, 3)
    print("Min-Cut minh hoa:")
    print("Max-Flow:", flow, "S:", S, "T:", T)
    print("Canh cat:", cut_edges, "Tong dung luong:", cut_cap)
    # Ly thuyet: trang thai dung pi = pi*P tuong duong P^T*pi^T = pi^T.
    # Vi vay pi^T la vector rieng cua P^T voi tri rieng lambda = 1.
