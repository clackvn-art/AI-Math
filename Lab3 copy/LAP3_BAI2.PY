def matrix_mul_2x2(A, B):
    return [
        [
            A[0][0] * B[0][0] + A[0][1] * B[1][0],
            A[0][0] * B[0][1] + A[0][1] * B[1][1]
        ],
        [
            A[1][0] * B[0][0] + A[1][1] * B[1][0],
            A[1][0] * B[0][1] + A[1][1] * B[1][1]
        ]
    ]


def matrix_power_fast(P, D_diag, P_inv, k):
    # Bước 1: D^k
    D_k = [
        [D_diag[0] ** k, 0.0],
        [0.0, D_diag[1] ** k]
    ]

    # Bước 2 và 3: P * D^k * P_inv
    return matrix_mul_2x2(
        matrix_mul_2x2(P, D_k),
        P_inv
    )


P = [
    [1, 1],
    [1, -1]
]

D_diag = [5, 2]

P_inv = [
    [0.5, 0.5],
    [0.5, -0.5]
]

print(matrix_power_fast(P, D_diag, P_inv, 3))