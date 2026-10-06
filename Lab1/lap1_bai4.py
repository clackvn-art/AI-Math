def matrix_multiply(A, B):
    # Số hàng và cột của A
    m = len(A)
    n = len(A[0])

    # Số hàng và cột của B
    n2 = len(B)
    p = len(B[0])

    # Kiểm tra điều kiện nhân ma trận
    if n != n2:
        print("Lỗi: Số cột của A phải bằng số hàng của B.")
        return None

    # Khởi tạo ma trận C kích thước m x p
    C = [[0 for _ in range(p)] for _ in range(m)]

    # Biến đếm số phép nhân
    multiplication_count = 0

    # 3 vòng lặp để nhân hai ma trận
    for i in range(m):
        for j in range(p):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]

                # Đếm phép nhân
                multiplication_count += 1

    # In tổng số phép nhân
    print("Tổng số phép nhân:", multiplication_count)

    return C


# Ma trận A
A = [
    [1, 2],
    [3, 4]
]

# Ma trận B
B = [
    [5, 6],
    [7, 8]
]

# Tính C = A x B
C = matrix_multiply(A, B)

# In ma trận A
print("Ma trận A:")
for row in A:
    print(row)

# In ma trận B
print("\nMa trận B:")
for row in B:
    print(row)

# In ma trận C
print("\nMa trận C = A x B:")
for row in C:
    print(row)