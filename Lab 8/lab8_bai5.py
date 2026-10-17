
import math


def loss(w1, w2):
    return (w1 - 3) ** 2 + (w2 - 3) ** 2


def project_to_segment(point, start, end):
    """Tim diem tren doan thang gan point nhat."""
    px, py = point
    ax, ay = start
    bx, by = end

    dx = bx - ax
    dy = by - ay
    length_squared = dx * dx + dy * dy

    if length_squared == 0:
        return start

    t = ((px - ax) * dx + (py - ay) * dy) / length_squared
    t = max(0.0, min(1.0, t))

    return ax + t * dx, ay + t * dy


def solve_constrained_l1():
    """
    Toi uu Loss voi |w1| + |w2| <= 2.

    Tim diem gan (3,3) nhat tren hinh thoi,
    bang cach duyet 4 canh va chieu diem len tung canh.
    """
    vertices = [
        (2.0, 0.0),
        (0.0, 2.0),
        (-2.0, 0.0),
        (0.0, -2.0)
    ]

    candidates = []

    for i in range(len(vertices)):
        start = vertices[i]
        end = vertices[(i + 1) % len(vertices)]

        point = project_to_segment((3.0, 3.0), start, end)
        candidates.append(point)

    # Goc (0,0) nam trong mien va co Loss = 18,
    # nhung diem toi uu se nam tren bien hinh thoi.
    best_point = min(candidates, key=lambda p: loss(*p))
    return best_point, loss(*best_point)


def solve_constrained_l2():
    """
    Toi uu Loss voi w1^2 + w2^2 <= 4.

    Diem toi uu la hinh chieu cua (3,3)
    len duong tron ban kinh 2.
    """
    norm = math.sqrt(3 ** 2 + 3 ** 2)
    w1 = 2 * 3 / norm
    w2 = 2 * 3 / norm

    return (w1, w2), loss(w1, w2)


if __name__ == "__main__":
    l1_point, l1_loss = solve_constrained_l1()
    l2_point, l2_loss = solve_constrained_l2()

    print("=== L1 (Lasso) ===")
    print("Diem toi uu:", tuple(round(v, 6) for v in l1_point))
    print("Loss:", round(l1_loss, 6))
    print("|w1| + |w2| =", round(
        abs(l1_point[0]) + abs(l1_point[1]), 6
    ))

    print("\n=== L2 (Ridge) ===")
    print("Diem toi uu:", tuple(round(v, 6) for v in l2_point))
    print("Loss:", round(l2_loss, 6))
    print("w1^2 + w2^2 =", round(
        l2_point[0] ** 2 + l2_point[1] ** 2, 6
    ))

    # Tong ket:
    # L1 co mien rang buoc hinh thoi voi cac dinh nam tren
    # truc toa do. Trong nhieu bai toan, cac goc nay giup
    # mot so he so bang 0, tao tinh thua (sparsity).
    #
    # L2 co mien rang buoc hinh tron tron tru, nen nghiem
    # thuong thu nho cac he so thay vi dua chung ve 0.
    #
    # Lien he 8 bai hoc:
    # Dai so tuyen tinh mo ta du lieu va phep bien doi;
    # do thi mo ta mang ket noi va cac luong;
    # xac suat mo hinh hoa bat dinh;
    # toi uu hoa tim cac tham so tot nhat cho mo hinh AI.
