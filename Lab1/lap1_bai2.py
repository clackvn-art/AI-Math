def norm_l1(v):
    # Tính chuẩn L1
    total = 0

    for x in v:
        total += abs(x)

    return total


def norm_l2(v):
    # Tính chuẩn L2
    sum_sq = 0

    for x in v:
        sum_sq += x ** 2

    return sum_sq ** 0.5


# Vector sai số
v = [-2, 3, -4, 5]

# Tính chuẩn L1
l1 = norm_l1(v)

# Tính chuẩn L2
l2 = norm_l2(v)

# In kết quả
print("Vector v:", v)
print("Chuẩn L1:", l1)
print("Chuẩn L2:", l2)