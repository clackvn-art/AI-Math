def gaussian_elimination(aug_matrix):
    # Sao chép ma trận để không làm thay đổi ma trận ban đầu
    A = [row[:] for row in aug_matrix]

    m = len(A)
    n = len(A[0])

    # Khử Gauss theo từng cột
    for k in range(min(m, n - 1)):

        # =========================
        # BƯỚC 1: Partial Pivoting
        # =========================

        # Tìm hàng có giá trị tuyệt đối lớn nhất ở cột k
        max_row = k

        for i in range(k + 1, m):
            if abs(A[i][k]) > abs(A[max_row][k]):
                max_row = i

        # Hoán đổi hàng
        if max_row != k:
            A[k], A[max_row] = A[max_row], A[k]

        # Nếu phần tử pivot gần bằng 0 thì bỏ qua
        if abs(A[k][k]) < 1e-12:
            continue

        # =========================
        # BƯỚC 2: Forward Elimination
        # =========================

        for i in range(k + 1, m):

            # Tính hệ số factor
            factor = A[i][k] / A[k][k]

            # Khử các phần tử phía dưới pivot
            for j in range(k, n):
                A[i][j] = A[i][j] - factor * A[k][j]

    # Làm tròn 2 chữ số thập phân
    for i in range(m):
        for j in range(n):
            A[i][j] = round(A[i][j], 2)

    return A


# Ma trận bổ sung [A|b]
augmented_matrix = [
    [2.0,  1.0, -1.0,  8.0],
    [-3.0, -1.0,  2.0, -11.0],
    [-2.0,  1.0,  2.0, -3.0]
]

# Gọi hàm khử Gauss
result = gaussian_elimination(augmented_matrix)

# In kết quả
print("Ma trận sau khi khử Gauss:")

for row in result:
    print(row)