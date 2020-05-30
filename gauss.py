def Gauss_sol(matrix: "list of list", result: list) -> list:
    n = len(matrix)

    for i in range(n):
        matrix[i] += [result[i]]
    
    for k in range(n - 1):
        for i in range(k + 1, n):
            div = matrix[i][k] / matrix[k][k]
            matrix[i][-1] -= div * matrix[k][-1]

            for j in range(k, n):
                matrix[i][j] -= div * matrix[k][j]

    x = [0 for i in range(n)]

    for k in range(n - 1, -1, -1):
        x[k] = (matrix[k][-1] - sum([matrix[k][j] * x[j] for j in range(k + 1, n)])) / matrix[k][k]

    for i in range(len(x)):
        x[i] = round(x[i]) if abs(x[i] - round(x[i])) < 10e-10 else round(x[i], 4)

    return x

test = [
    [5, 2, 1],
    [2, 7, 2],
    [1, 2, 5]
]

test_result = [15, 17, 19]

print(Gauss_sol(test, test_result))