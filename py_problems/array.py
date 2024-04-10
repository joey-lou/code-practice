from typing import List


def fix_array(array: List[int], len_a: int, len_b: int):
    def fix_array_recursive(array: List[int], start_idx: int, len_a: int, len_b: int):
        ai = len_b + start_idx  # index where a currently starts
        bi = start_idx  # index of where b current is
        for _ in range(swaps := min(len_a, len_b)):
            array[ai], array[bi] = array[bi], array[ai]
            ai += 1
            bi += 1

        if len_a > len_b:
            len_a, len_b = len_a - len_b, len_a
        else:
            len_a, len_b = len_b, len_b - len_a

        start_idx += swaps
        if len_a and len_b:
            fix_array_recursive(array, start_idx, len_a, len_b)

    fix_array_recursive(array, 0, len_a, len_b)


A = [1, 2, 3, 4, 5, 6]
B = [7, 8]

P = B + A
print(P)
fix_array(P, len(A), len(B))
print(P)
