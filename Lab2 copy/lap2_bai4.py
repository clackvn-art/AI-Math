import math


# Hàm co giãn các điểm
def scale_points(points, sx, sy):
    result = []

    for x, y in points:
        new_x = x * sx
        new_y = y * sy

        result.append([
            round(new_x, 2),
            round(new_y, 2)
        ])

    return result


# Hàm xoay các điểm
def rotate_points(points, angle_degrees):
    # Đổi độ sang radian
    rad = math.radians(angle_degrees)

    # Ma trận xoay
    R = [
        [math.cos(rad), -math.sin(rad)],
        [math.sin(rad), math.cos(rad)]
    ]

    result = []

    for x, y in points:
        # Nhân ma trận R với vector điểm [x, y]
        new_x = R[0][0] * x + R[0][1] * y
        new_y = R[1][0] * x + R[1][1] * y

        result.append([
            round(new_x, 2),
            round(new_y, 2)
        ])

    return result


# Dữ liệu mẫu
points = [
    [1, 0],
    [0, 1],
    [2, 2]
]

# Co giãn
scaled = scale_points(points, 2, 3)

# Xoay 90 độ
rotated = rotate_points(points, 90)

print("Điểm ban đầu:", points)
print("Sau khi co giãn:", scaled)
print("Sau khi xoay 90 độ:", rotated)