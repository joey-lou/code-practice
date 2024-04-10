class Solution:
    # No.172 find number of trailing zeros of factorial
    def trailingZeroes(self, n: int) -> int:
        # by pattern, we can find the period where number of fives' contrib repeat
        base = 1
        retval = 0
        while periods := n // (5**base):
            retval += periods
            base += 1
        return retval


if __name__ == "__main__":
    print(Solution().trailingZeroes(100))
