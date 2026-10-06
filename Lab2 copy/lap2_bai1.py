def compute_linear_combination(B, c):
    # Bước 1: Xác định số chiều
    dim = len(B[0])

    # Bước 2: Khởi tạo vector kết quả
    v = [0.0] * dim

    # Bước 3: Duyệt qua từng vector cơ sở
    for i in range(len(B)):
        # Bước 4: Cộng c[i] * B[i][j] vào v[j]
        for j in range(dim):
            v[j] += c[i] * B[i][j]

    # Bước 5: Trả về kết quả
    return v


# Dữ liệu đầu vào
B = [
    [1, 0],  # b1
    [1, 1]   # b2
]

c = [-2, 7]

# Tính tổ hợp tuyến tính
v = compute_linear_combination(B, c)

# In kết quả
print("Vector v =", v)