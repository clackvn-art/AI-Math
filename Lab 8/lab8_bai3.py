
def build_dual(c, A, b):
    """
    Primal:
        max c^T x
        A x <= b, x >= 0

    Dual:
        min b^T y
        A^T y >= c, y >= 0

    Tra ve:
        dual_c: he so ham muc tieu doi ngau
        dual_A: ma tran rang buoc doi ngau
        dual_b: vector ve phai
    """
    m = len(A)
    n = len(c)

    if len(b) != m:
        raise ValueError("Do dai b phai bang so hang cua A.")

    if any(len(row) != n for row in A):
        raise ValueError("So cot cua A phai bang len(c).")

    # Chuyen A thanh ma tran chuyen vi A^T
    A_transpose = [
        [A[i][j] for i in range(m)]
        for j in range(n)
    ]

    dual_c = list(b)
    dual_A = A_transpose
    dual_b = list(c)

    return dual_c, dual_A, dual_b


def evaluate_objective(coefficients, values):
    return sum(c * x for c, x in zip(coefficients, values))


if __name__ == "__main__":
    # Bai toan goc cua Lab 8
    c = [40, 30]
    A = [
        [2, 1],
        [1, 1]
    ]
    b = [100, 80]

    dual_c, dual_A, dual_b = build_dual(c, A, b)

    print("Bai toan doi ngau:")
    print("Minimize:", dual_c)
    print("Ma tran rang buoc A^T:")
    for row in dual_A:
        print(row)
    print("Vector rang buoc:", dual_b)
    print("Dieu kien: A^T*y >= c, y >= 0")

    # Nghiem toi uu cua bai toan goc
    x_star = [20, 60]
    primal_value = evaluate_objective(c, x_star)

    # Nghiem toi uu doi ngau
    y_star = [10, 20]
    dual_value = evaluate_objective(b, y_star)

    print("\nGia tri toi uu bai toan goc:", primal_value)
    print("Gia tri toi uu bai toan doi ngau:", dual_value)
    print("Doi ngau manh:", primal_value == dual_value)
