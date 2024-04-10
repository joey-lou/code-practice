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
        return res


# Test Matrix Class
# A = Matrix(3, 3)
# B = [[1, 2], [4, 5], [7, 8]]
# B = Matrix(B)

# print(B.X)
# A.fill(2, 2, 1)
# A.fill(1, 1, 1)
# A.fill(0, 0, 1)


# print(A.X)
# print(A.multiply(B))
from collections import defaultdict


class SparseMatrix:
    def __init__(self, *argv):
        assert (
            len(argv) == 3 or len(argv) == 2
        ), "Arguments: m, n, dictionary of index:value"

        if len(argv) == 3:
            self.X = copy.deepcopy(argv[2])
            self.r_c = defaultdict(set)
            self.c_r = defaultdict(set)
            for r, c in self.X.keys():
                self.r_c[r].add(c)
                self.c_r[c].add(r)
            self.m = argv[0]
            self.n = argv[1]
        else:
            m, n = argv
            self.m, self.n = m, n
            self.r_c = defaultdict(set)
            self.c_r = defaultdict(set)
            self.X = {}

    def fill(self, i, j, val):
        assert 0 <= i < self.m and 0 <= j < self.n, "Index Error"
        self.X[(i, j)] = val
        self.r_c[i].add(j)
        self.c_r[j].add(i)

    def multiply(self, B):
        # multiply by another matrix object
        assert self.n == B.m, "Matrix dimension mismatch"
        res = [[0] * B.n for _ in range(self.m)]

        for i in self.r_c:
            for j in B.c_r:
                summ = 0
                for k in self.r_c[i] & B.c_r[j]:
                    summ += self.X[(i, k)] * B.X[(k, j)]
                if summ != 0:
                    res[i][j] = summ
        return res


C = SparseMatrix(3, 30)
C.fill(0, 0, 1)
D = SparseMatrix(30, 10, {(1, 1): 10, (0, 0): 20})

print(C.multiply(D))

# print(C.X, C.m, C.n)
