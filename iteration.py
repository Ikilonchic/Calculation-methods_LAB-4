import numpy as np

def Richardson_sol(matrix, result, true_xs, epsilon=0.1) -> list:
    if np.linalg.det(np.array(matrix)) == 0:
        return None
    
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
    xs_new = B.dot(xs_prev) + g

    while np.linalg.norm(true_xs - xs_prev) > epsilon:
        xs_new = np.array(B.dot(xs_prev) + g)
        xs_prev = xs_new

    xs_new = xs_new.tolist()

    for i in range(len(xs_new)):
        xs_new[i] = round(xs_new[i]) if abs(xs_new[i] - round(xs_new[i])) < 10e-10 else round(xs_new[i], 4)

    return xs_new

test = [
    [5, 2, 1],
    [2, 7, 2],
    [1, 2, 5]
]

test_result = [15, 17,19]

print(Richardson_sol(test, test_result, [2, 1, 3]))