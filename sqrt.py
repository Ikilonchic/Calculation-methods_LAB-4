from math import sqrt

def SQRT_sol(matrix: list, result: list) -> list:
    n = len(result)

    S = [[0.0 for i in range(n)] for j in range(n)]

    for i in range(n):
        for j in range(i, n):
            if i == j:
                S[i][i] = sqrt(matrix[i][i] - sum([S[k][i] ** 2 for k in range(0, i) if i >= 1]))
            else:
                S[i][j] = (matrix[i][j] - sum([S[k][i] * S[k][j] for k in range(0, i)])) / (S[i][i])

    Y = [0.0 for i in range(n)]

    for i in range(n):
        if i == 0:
            Y[i] = (result[i]) / (S[i][i])
        else:
            Y[i] = (result[i] - sum([S[k][i] * Y[k] for k in range(0, i)])) / (S[i][i])

    X = [0.0 for i in range(n)]

    for i in range(n - 1, -1, -1):
        if i == n - 1:
            X[i] = (Y[i]) / (S[i][i])
        else:
            X[i] = (Y[i] - sum([S[i][k] * X[k] for k in range(i, n)])) / (S[i][i])

    for i in range(n):
        X[i] = round(X[i]) if abs(X[i] - round(X[i])) < 10e-10 else round(X[i], 4)


    return X

if __name__ == "__main__":
    test = [
        [5, 2, 1],
        [2, 7, 2],
        [1, 2, 5]
    ]

    test_result = [15, 17, 19]

    print(SQRT_sol(test, test_result))