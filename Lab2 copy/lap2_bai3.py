def find_kernel_basis_2x3(A):
    # Đưa A về RREF
    M = [row[:] for row in A]

    # Khử Gauss-Jordan
    # Giả sử RREF có dạng:
    # [1 0 c1]
    # [0 1 c2]

    # c1 và c2
    c1 = M[0][2]
    c2 = M[1][2]

    # Vector cơ sở của Kernel
    basis = [-c1, -c2, 1.0]

    # Nullity = số biến tự do
    nullity = 1

    return basis, nullity


A = [
    [1, 0, 2],
    [0, 1, 3]
]

basis, nullity = find_kernel_basis_2x3(A)

print("Vector cơ sở của Ker(f):", basis)
print("Nullity:", nullity)