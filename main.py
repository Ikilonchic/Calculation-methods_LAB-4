if __name__ != "__main__":
    exit()

from sqrt import SQRT_sol
from iteration import Richardson_sol
from gauss import Gauss_sol

test = [
    [5, 2, 1],
    [2, 7, 2],
    [1, 2, 5]
]

test_result = [15, 17,19]

print(SQRT_sol(test, test_result))
print(Gauss_sol(test, test_result))
print(Richardson_sol(test, test_result, SQRT_sol(test, test_result)))