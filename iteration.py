import numpy as np
from copy import deepcopy

def Richardson_sol(matrix: list, result: list, true_xs: list, epsilon=10e-10) -> list:
    n = len(result)
    B = np.array(matrix)
    g = np.array(result)

    for i in range(n):
        for j in range(n):
            if i != j:
                B[i][j] /= -B[i][i]
        g[i] /= B[i][i]
        B[i][i] = 0.0

    xs_prev = np.array([1.0] * n)
    xs_new = B.dot(xs_prev) + deepcopy(g)

    while np.linalg.norm(true_xs - xs_prev) > epsilon:
        xs_new = np.array(B.dot(xs_prev) + deepcopy(g))
        xs_prev = xs_new

    xs_new = xs_new.tolist()

    for i in range(len(xs_new)):
        xs_new[i] = round(xs_new[i]) if abs(xs_new[i] - round(xs_new[i])) < 10e-10 else round(xs_new[i], 4)

    return xs_new

if __name__ == "__main__":
    test = [
        [5, 2, 1],
        [2, 7, 2],
        [1, 2, 5]
    ]

    test_result = [15, 17, 19]

    print(Richardson_sol(test, test_result, [2, 1, 3]))