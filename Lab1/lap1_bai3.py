def matrix_vector_multiply(W, x):
    # Kiểm tra số cột của W có bằng số phần tử của x không
    rows = len(W)
    cols = len(W[0])

    if cols != len(x):
        print("Lỗi: Số cột của W phải bằng số phần tử của x.")
        return None

    # Tạo vector kết quả y gồm m phần tử
    y = [0 for _ in range(rows)]

    # Tính y = W * x
    for i in range(rows):
        for j in range(cols):
            y[i] += W[i][j] * x[j]

    return y


# Ma trận W
W = [
    [1, 2, 3],
    [4, 5, 6]
]

# Vector x
x = [1, 2, 3]

# Tính y = W * x
y = matrix_vector_multiply(W, x)

# In kết quả
print("Ma trận W:")
for row in W:
    print(row)

print("Vector x:", x)
print("Vector y = W * x:", y)