def gauss(matrix) -> list:
    n = len(matrix)
    
    for k in range(n - 1):
        for i in range(k + 1, n):
            div = matrix[i][k] / matrix[k][k]
            matrix[i][-1] -= div * matrix[k][-1]

            for j in range(k, n):
                matrix[i][j] -= div * matrix[k][j]

    x = [0 for i in range(n)]

    for k in range(n - 1, -1, -1):
        x[k] = (matrix[k][-1] - sum([matrix[k][j] * x[j] for j in range(k + 1, n)])) / matrix[k][k]

    return x