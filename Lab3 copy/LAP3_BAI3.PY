def mean_centering(X):
    # Số hàng và số cột
    M = len(X)
    N = len(X[0])

    # Bước 1: Tính trung bình từng cột
    mean = [0.0] * N

    for j in range(N):
        total = 0.0

        for i in range(M):
            total += X[i][j]

        mean[j] = total / M

    # Bước 2: Trừ trung bình từng cột
    X_centered = []

    for i in range(M):
        row = []

        for j in range(N):
            row.append(X[i][j] - mean[j])

        X_centered.append(row)

    return X_centered


def compute_covariance_matrix(X_centered):
    # Số mẫu và số đặc trưng
    M = len(X_centered)
    N = len(X_centered[0])

    # Khởi tạo ma trận covariance N x N
    Cov = []

    for i in range(N):
        row = [0.0] * N
        Cov.append(row)

    # Tính Cov[i][j]
    for i in range(N):
        for j in range(N):

            total = 0.0

            for k in range(M):
                total += X_centered[k][i] * X_centered[k][j]

            Cov[i][j] = total / (M - 1)

    return Cov


# Dữ liệu mẫu
X = [
    [1, 2],
    [2, 4],
    [3, 6],
    [4, 8]
]

# Bước 1: Trừ trung bình
X_centered = mean_centering(X)

# Bước 2: Tính ma trận hiệp phương sai
Cov = compute_covariance_matrix(X_centered)

print("Ma trận sau khi trừ trung bình:")

for row in X_centered:
    print([round(value, 2) for value in row])

print("\nMa trận hiệp phương sai:")

for row in Cov:
    print([round(value, 2) for value in row])