def is_linearly_dependent_2d(v1, v2):
    # Tính định thức
    det = v1[0] * v2[1] - v1[1] * v2[0]

    # Nếu định thức gần bằng 0 -> phụ thuộc tuyến tính
    if abs(det) < 1e-9:
        return True

    # Ngược lại -> độc lập tuyến tính
    return False


# Kiểm tra
print(is_linearly_dependent_2d([2, 4], [4, 8]))  # True
print(is_linearly_dependent_2d([2, 4], [1, 5]))  # False