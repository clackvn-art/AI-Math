import math


# Hàm tạo ma trận biến đổi Affine 3x3
def create_affine_matrix(sx, sy, angle_deg, tx, ty):
    # Đổi độ sang radian
    rad = math.radians(angle_deg)

    # Tính sin và cos
    cos_a = math.cos(rad)
    sin_a = math.sin(rad)

    # Ma trận Affine 3x3
    matrix = [
        [sx * cos_a, -sy * sin_a, tx],
        [sx * sin_a,  sy * cos_a, ty],
        [0,          0,          1]
    ]

    return matrix


# Hàm biến đổi Bounding Box
def transform_bounding_box(bbox, affine_matrix):
    x, y = bbox

    # Chuyển tọa độ sang tọa độ đồng nhất
    point = [x, y, 1]

    # Nhân ma trận 3x3 với vector [x, y, 1]
    new_x = (
        affine_matrix[0][0] * point[0]
        + affine_matrix[0][1] * point[1]
        + affine_matrix[0][2] * point[2]
    )

    new_y = (
        affine_matrix[1][0] * point[0]
        + affine_matrix[1][1] * point[1]
        + affine_matrix[1][2] * point[2]
    )

    # Làm tròn 2 chữ số
    return [round(new_x, 2), round(new_y, 2)]


# Dữ liệu mẫu
bbox = [10, 20]

# Tạo ma trận:
# Co giãn x2, y2
# Xoay 90 độ
# Tịnh tiến (5, 10)
affine_matrix = create_affine_matrix(
    2,      # sx
    2,      # sy
    90,     # angle_deg
    5,      # tx
    10      # ty
)

# Biến đổi bounding box
new_bbox = transform_bounding_box(
    bbox,
    affine_matrix
)

print("Ma trận Affine 3x3:")
for row in affine_matrix:
    print(row)

print("Bounding Box ban đầu:", bbox)
print("Bounding Box sau biến đổi:", new_bbox)