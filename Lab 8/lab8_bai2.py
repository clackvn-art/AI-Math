
def convert_to_standard_form(c, A_ub, b_ub):
    """
    Bai toan goc:
        max c^T * x
        A_ub * x <= b_ub
        x >= 0

    Chuyen thanh:
        A_eq * z = b_eq
        z >= 0

    z gom cac bien goc va bien bu.
    Ham muc tieu doi dau de chuyen max thanh min.
    """
    m = len(A_ub)
    n = len(c)

    if len(b_ub) != m:
        raise ValueError("So phan tu b_ub phai bang so rang buoc.")

    if any(len(row) != n for row in A_ub):
        raise ValueError("Moi hang cua A_ub phai co len(c) phan tu.")

    # Them m cot bien bu vao ma tran
    A_eq = []

    for i in range(m):
        row = list(A_ub[i]) + [0] * m
        row[n + i] = 1
        A_eq.append(row)

    b_eq = list(b_ub)

    # Minimize -c^T*x, bien bu co he so 0
    c_std = [-value for value in c] + [0] * m

    return A_eq, b_eq, c_std


if __name__ == "__main__":
    c = [40, 30]
    A_ub = [
        [2, 1],
        [1, 1]
    ]
    b_ub = [100, 80]

    A_eq, b_eq, c_std = convert_to_standard_form(
        c, A_ub, b_ub
    )

    print("Ma tran A_eq:")
    for row in A_eq:
        print(row)

    print("Vector b_eq:", b_eq)
    print("Vector c_std:", c_std)
    print("Cac bien moi: x1, x2, s1, s2")
