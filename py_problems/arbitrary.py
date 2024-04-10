from collections import deque
from typing import Any


def is_neighbor(a: str, b: str) -> bool:
    diff_cnt = 0
    for i, j in zip(a, b):
        if i == j:
            pass
        elif diff_cnt == 0:
            diff_cnt += 1
        else:
            return False
    return diff_cnt == 1


class PriorityQueue:
    def __init__(self, min_heap: bool = True) -> None:
        self.heap = []
        self._sign = 1 if min_heap else -1
        self._item_to_idx = {}

    def insert(self, hashable: Any, value: int) -> None:
        if hashable in self._item_to_idx:
            # pop
            ...

    def _swap(self, item_a: Any, item_b: Any) -> None:
        # simply swap elements, does not garantee heap structure
        self._item_to_idx[item_b], self._item_to_idx[item_a] = (
            self._item_to_idx[item_a],
            self._item_to_idx[item_b],
        )


def check_loop_condition():
    queue = deque([1])
    while queue:
        popped = []
        for _ in range(len(queue)):
            i = queue.popleft()
            if i == 5:
                return
            [queue.append(i + 1) for _ in range(i)]
            popped.append(i)
        print(popped)


import copy


class Matrix:
    def __init__(self, *argv):
        if len(argv) == 1:
            self.X = copy.deepcopy(argv[0])
            self.m = len(self.X)
            self.n = len(self.X[0])
        elif len(argv) == 2:
            m, n = argv
            self.m, self.n = m, n
            self.X = [[0] * n for _ in range(m)]
        else:
            print("Argument either an array or specific matrix dimension")

    def fill(self, i, j, val):
        assert 0 <= i < self.m and 0 <= j < self.n, "Index Error"
        self.X[i][j] = val

    def multiply(self, B):
        # multiply by another matrix object
        assert self.n == B.m, "Matrix dimension mismatch"
        res = [[0] * B.n for _ in range(self.m)]
        for i in range(self.m):
            for j in range(B.n):
                summ = 0
                for k in range(self.n):
                    summ += self.X[i][k] * B.X[k][j]
                res[i][j] = summ
        return Matrix(res)

    def get(self, i, j):
        return self.X[i][j]

    def __mul__(self, other):
        return self.multiply(other)

    def __repr__(self) -> str:
        return str(self.X)


def fibonnaci_matrix(n: int):
    # O(logn)
    if n == 1:
        return Matrix([[1, 1], [1, 0]])
    if n % 2:
        A = fibonnaci_matrix((n - 1) / 2)
        return A * A * Matrix([[1, 1], [1, 0]])
    else:
        A = fibonnaci_matrix(n / 2)
        return A * A


def fibonnaci(n: int):
    return fibonnaci_matrix(n).get(1, 0)


def fibonnaci_dumb(n: int):
    # O(^n)
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonnaci_dumb(n - 1) + fibonnaci_dumb(n - 2)


def fibonnaci_dp(n: int):
    # O(n)
    if n == 0:
        return 0
    if n == 1:
        return 1
    dp = [0, 1]
    for i in range(2, n + 1):
        dp[0], dp[1] = dp[1], dp[0] + dp[1]
    return dp[1]


if __name__ == "__main__":
    x = 9
    print(fibonnaci(x), fibonnaci_dumb(x), fibonnaci_dp(x))
