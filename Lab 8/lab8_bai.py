
def solve_lp_geometric(vertices, c1, c2):
    best_val = float("-inf")
    best_vertex = None

    for x1, x2 in vertices:
        current_val = c1 * x1 + c2 * x2
        print(f"Dinh ({x1}, {x2}) -> f = {current_val}")

        if current_val > best_val:
            best_val = current_val
            best_vertex = (x1, x2)

    return best_vertex, best_val


if __name__ == "__main__":
    vertices = [(0, 0), (0, 80), (20, 60), (50, 0)]
    c1, c2 = 40, 30

    optimal_point, max_profit = solve_lp_geometric(
        vertices, c1, c2
    )

    print("\nNghiem toi uu:", optimal_point)
    print("Loi nhuan toi da:", max_profit, "USD")
