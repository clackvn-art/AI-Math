def transpose_matrix(A):
    # Bước 1: Xác định số hàng và số cột
    rows = len(A)
    cols = len(A[0])

    # Bước 2: Khởi tạo ma trận chuyển vị
    A_T = [[0 for _ in range(rows)] for _ in range(cols)]

    # Bước 3: Duyệt qua từng hàng và từng cột
    for i in range(rows):
        for j in range(cols):

            # Bước 4: Đổi hàng thành cột
            A_T[j][i] = A[i][j]

    # Bước 5: Trả về ma trận chuyển vị
    return A_T


# Ma trận đầu vào A (2 x 3)
A = [
    [1, 2, 3],
    [4, 5, 6]
]

# Gọi hàm chuyển vị
A_T = transpose_matrix(A)

# In ma trận ban đầu
print("Ma trận A:")
for row in A:
    print(row)

# In ma trận chuyển vị
print("\nMa trận chuyển vị A^T:")
for row in A_T:
    print(row)