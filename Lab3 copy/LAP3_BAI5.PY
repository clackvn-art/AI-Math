import numpy as np

# ==========================================
# BÀI 5: PCA GIẢM CHIỀU DỮ LIỆU BỆNH ÁN
# ==========================================

# Dữ liệu:
# [Huyết áp, Đường huyết, Cholesterol, BMI]
medical_data = np.array([
    [120, 95, 210, 24.5],
    [140, 130, 250, 29.0],
    [110, 85, 180, 21.5],
    [155, 160, 280, 32.0],
    [130, 105, 220, 26.0]
], dtype=float)


# ==========================================
# 1. HÀM PCA GIẢM CHIỀU VỀ 2D
# ==========================================

def pca_reduce_2d(data):
    # Bước 1: Tính trung bình từng cột
    mean = np.mean(data, axis=0)

    # Bước 2: Trừ trung bình (Centering)
    centered_data = data - mean

    # Bước 3: Tính ma trận hiệp phương sai
    covariance_matrix = np.cov(centered_data, rowvar=False)

    # Bước 4: Tính trị riêng và vector riêng
    eigenvalues, eigenvectors = np.linalg.eigh(covariance_matrix)

    # Bước 5: Sắp xếp trị riêng từ lớn đến nhỏ
    index = np.argsort(eigenvalues)[::-1]

    eigenvalues = eigenvalues[index]
    eigenvectors = eigenvectors[:, index]

    # Bước 6: Chọn 2 vector riêng lớn nhất (PC1, PC2)
    principal_components = eigenvectors[:, :2]

    # Bước 7: Chiếu dữ liệu lên 2 thành phần chính
    reduced_data = centered_data @ principal_components

    return reduced_data, covariance_matrix, eigenvalues


# Gọi hàm PCA
reduced_data, covariance_matrix, eigenvalues = pca_reduce_2d(
    medical_data
)


# ==========================================
# 2. IN KẾT QUẢ PCA
# ==========================================

print("===== KẾT QUẢ PCA =====")

print("\nMa trận hiệp phương sai 4x4:")
print(covariance_matrix)

print("\nCác trị riêng (Eigenvalues):")
print(eigenvalues)

print("\nDữ liệu sau khi giảm từ 4 chiều xuống 2 chiều:")
print(reduced_data)


# ==========================================
# 3. TÍNH TỶ LỆ PHƯƠNG SAI ĐƯỢC GIẢI THÍCH
# ==========================================

lambda_1 = 145.2
lambda_2 = 32.8
lambda_3 = 4.5
lambda_4 = 1.2

total_variance = lambda_1 + lambda_2 + lambda_3 + lambda_4

ratio = (lambda_1 + lambda_2) / total_variance

print("\n===== EXPLAINED VARIANCE =====")
print("Tổng phương sai:", total_variance)
print("Tỷ lệ phương sai giữ lại:", ratio)
print("Tỷ lệ phần trăm:", ratio * 100, "%")


# ==========================================
# 4. NHẬN XÉT Ý NGHĨA
# ==========================================

# Nếu tỷ lệ thông tin giữ lại > 90%,
# việc giảm từ 4 chiều xuống 2 chiều vẫn giữ
# phần lớn thông tin quan trọng của dữ liệu.
#
# PCA giúp giảm số chiều dữ liệu, từ đó dễ dàng
# trực quan hóa dữ liệu bệnh nhân trên biểu đồ 2D.
#
# Đối với chuyên gia y tế, biểu đồ 2D giúp quan sát
# sự phân bố, nhóm bệnh nhân và phát hiện các điểm
# dữ liệu bất thường một cách trực quan hơn.