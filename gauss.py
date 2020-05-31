from copy import deepcopy

def Gauss_sol(matrix: list, result: list) -> list:
    n = len(matrix)
    system = deepcopy(matrix)

    for i in range(n):
        system[i] += deepcopy([float(result[i])])
    
    for k in range(n - 1):
        for i in range(k + 1, n):
            div = system[i][k] / system[k][k]
            system[i][-1] -= div * system[k][-1]

            for j in range(k, n):
                system[i][j] -= div * system[k][j]

    x = [0 for i in range(n)]

    for k in range(n - 1, -1, -1):
        x[k] = (system[k][-1] - sum([system[k][j] * x[j] for j in range(k + 1, n)])) / system[k][k]

    for i in range(len(x)):
        x[i] = round(x[i]) if abs(x[i] - round(x[i])) < 10e-10 else round(x[i], 4)

    return x

if __name__ == "__main__":
    test = [
        [5, 2, 1],
        [2, 7, 2],
        [1, 2, 5]
    ]

    test_result = [15, 17, 19]

    print(Gauss_sol(test, test_result))