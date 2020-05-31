if __name__ != "__main__":
    exit()

from sqrt import SQRT_sol
from iteration import Richardson_sol
from gauss import Gauss_sol

test = [
    [7., -1., -3.],
    [-1., 5., -2.],
    [-3., -2., 7.]
]

test_result = [14., -2., 3.]

print(f"Результат метода квадратного корня: {SQRT_sol(test, test_result)}")
print(f"Результат метода Гаусса: {Gauss_sol(test, test_result)}")
print(f"Результат метода простой итерации: {Richardson_sol(test, test_result, SQRT_sol(test, test_result))}")
