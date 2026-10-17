# Bai 4: Maximum Bipartite Matching quy doi sang Max-Flow
from lab7_bai3 import ford_fulkerson

def solve_bipartite_matching(L, R, candidate_edges):
    L, R = list(L), list(R)
    li = {u:i for i,u in enumerate(L)}
    ri = {v:len(L)+i for i,v in enumerate(R)}
    source, sink = len(L)+len(R), len(L)+len(R)+1
    n = sink + 1
    C = [[0]*n for _ in range(n)]
    for u in L: C[source][li[u]] = 1
    for u,v in candidate_edges:
        if u in li and v in ri: C[li[u]][ri[v]] = 1
    for v in R: C[ri[v]][sink] = 1
    flow, _ = ford_fulkerson(C, source, sink)
    return flow

if __name__ == "__main__":
    L, R = [0,1], [2,3]
    edges = [(0,2), (0,3), (1,2)]
    print("So cap ghep toi da:", solve_bipartite_matching(L, R, edges)) # 2
