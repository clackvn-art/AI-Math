# Bai 1: Chuoi Markov va trang thai dung
def simulate_markov_chain(P, pi_0, num_steps=50):
    n = len(pi_0)
    pi = list(pi_0)
    for _ in range(num_steps):
        pi = [sum(pi[i] * P[i][j] for i in range(n)) for j in range(n)]
    return [round(x, 4) for x in pi]

def stationary_distribution(P, tol=1e-12, max_iter=10000):
    n = len(P)
    pi = [1 / n] * n
    for _ in range(max_iter):
        nxt = [sum(pi[i] * P[i][j] for i in range(n)) for j in range(n)]
        if max(abs(nxt[i] - pi[i]) for i in range(n)) < tol:
            return [round(x, 4) for x in nxt]
        pi = nxt
    return [round(x, 4) for x in pi]

if __name__ == "__main__":
    P = [[0.8, 0.2], [0.4, 0.6]]
    pi0 = [1.0, 0.0]
    print("Sau 50 buoc (Nang, Mua):", simulate_markov_chain(P, pi0, 50))
    print("Trang thai dung:", stationary_distribution(P))
    # Ket qua: [0.6667, 0.3333]
