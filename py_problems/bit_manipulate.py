from typing import List

import numpy as np

N = 8


# binaries are stored with least significant bit at smallest index (little endianish)
def decimal_to_binary(dec_num: int, bin_array: np.ndarray) -> np.ndarray:
    i = 0
    bin_array.fill(0)  # fill 0 to be sure
    sign_bit = 1 if dec_num < 0 else 0
    abs_num = dec_num if dec_num > 0 else -dec_num
    for i in range(n := len(bin_array)):
        bin_array[i] = abs_num % 2
        abs_num >>= 1
        if abs_num == 0:
            break
    if sign_bit:
        # invert
        bin_array = 1 - bin_array
        # add 1 until there is no need
        for i in range(n):
            bin_array[i] += 1
            remainder = bin_array[i] // 2
            bin_array[i] %= 2
            if remainder == 0:
                break
    return bin_array


def binary_to_decimal(bin_array: np.ndarray) -> int:
    n = len(bin_array)
    sign_bit = bin_array[n - 1]
    if sign_bit:
        for i in range(n):
            bin_array[i] -= 1
            remainder = bin_array[i] // 2
            bin_array[i] %= 2
            if remainder == 0:
                break
        bin_array = 1 - bin_array
    num = 0
    for i in range(n - 1, -1, -1):
        num <<= 1
        num += bin_array[i]
    if sign_bit:
        num = -num
    return num


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        bits = np.zeros(N, dtype=np.int16)
        tmp = np.zeros(N, dtype=np.int16)
        for num in nums:
            bits += decimal_to_binary(num, tmp)

        bits %= 3
        return binary_to_decimal(bits)

    def singleNumberFaster(self, nums: List[int]) -> int:
        # instead of constructing binary representation in array format ourselves
        # take advantage of the underlying representation in c and use bitwise
        # operation in python directly

        # for instance x | y for integers will do a bitwise or
        ans = 0

        for i in range(N):
            bit = 0
            for num in nums:
                bit += (num >> i) & 1
            bit %= 3
            ans |= bit << i

        # because we do not prevent answer to grow beyond N digits in python
        # as python can have inf length ints, python would intepret the binary bits
        # as if they were usigned ints, we need to convert them to signed by subtracting the
        # total numbers range given the bits, for 4 bits that is 2**4=16 for instance
        if ans >= 2 ** (N - 1):
            ans -= 2**N
            print("?")
        return ans

    def singleNumberFastest(self, nums: List[int], expected_repeat: int = 3) -> int:
        # use finite state machine to describe the possible outcomes
        states = [0] * (expected_repeat - 1)
        for num in nums:
            for i in range(expected_repeat - 1):
                others = 0
                for j in range(expected_repeat - 1):
                    if i == j:
                        continue
                    others |= states[j]
                states[i] = (num ^ states[i]) ^ others
        for i in range(expected_repeat - 1):
            if states[i]:
                print(states[i], f"repeated {i+1} times")
        return states[0]


if __name__ == "__main__":
    ans = Solution().singleNumberFastest([1, 1, 1, -100, -100, -100, 123, 99, 99, 99])
    print(ans)
