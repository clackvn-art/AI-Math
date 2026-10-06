def verify_eigen(A, x, lambda_val):
    # Bước 1: Tính A * x
    lhs = []

    for row in A:
        total = 0

        for i in range(len(x)):
            total += row[i] * x[i]

        lhs.append(total)

    # Bước 2: Tính lambda * x
    rhs = []

    for value in x:
        rhs.append(lambda_val * value)

    # Bước 3: So sánh hai vector
    for i in range(len(x)):
        if abs(lhs[i] - rhs[i]) >= 1e-6:
            return False

    # Bước 4: Nếu giống nhau -> là vector riêng
    return True


# Dữ liệu đầu vào
A = [
    [4, 2],
    [1, 3]
]

x = [2, 1]

lambda_val = 5

# Kiểm tra
result = verify_eigen(A, x, lambda_val)

print("Kết quả:", result)