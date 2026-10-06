def project_data_1d(X_centered, pc_vector):
    result = []

    for row in X_centered:
        value = 0
        for i in range(len(row)):
            value += row[i] * pc_vector[i]
        result.append(value)

    return result
X_centered = [
    [1, 2],
    [3, 4],
    [5, 6]
]

pc_vector = [0.6, 0.8]

print(project_data_1d(X_centered, pc_vector))