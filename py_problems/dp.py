from typing import List


class Solution:
    # 97.
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        """We create a matrix A of size (m+1)x(n+1) to store the state of interleave,
            where m = len(s1), n = len(s2)
        A[i][j] = 1, if we can interleave successfully using symbols till index i-1 on s1 and j-1 on s2
            to construct a substring that is s3[:i+j]
        A[i][j] = 0, simply means that is not possible

        We will need to populate the matrix from upper left corner and onwards, simply check the last element in matrix
        """
        m = len(s1)
        n = len(s2)
        l = len(s3)
        if l != m + n:
            return False

        A = [[0] * (n + 1) for _ in range(m + 1)]
        A[0][0] = 1
        for i in range(m + 1):
            for j in range(n + 1):
                k = i + j - 1
                if i > 0 and A[i - 1][j] == 1 and s3[k] == s1[i - 1]:
                    # top node is good
                    A[i][j] = 1
                elif j > 0 and A[i][j - 1] == 1 and s3[k] == s2[j - 1]:
                    # left node is good
                    A[i][j] = 1
        return A[m][n]


class Solution:
    # no.123 best time to buy and sell stock twice given list of prices
    # can not run two transaction on a single day
    def maxProfit(self, prices: List[int]) -> int:
        """for a single buy/sell pair, the answer is straightforward, we can find the low
        and subsequent high of a series in O(N):
        iterate through list:
            record the lowest point till current index
            compare current price against that lowest price
            update max profit and lowest price since

        in case of two actions, we can run the above algo in two sequences, one from left to right
        the other in reverse
        """
        l2r_min = float("inf")
        r2l_max = float("-inf")
        N = len(prices)
        l2r_best = N * [0]
        for i in range(N):
            l2r_min = min(prices[i], l2r_min)
            l2r_best[i] = prices[i] - l2r_min

        retval = l2r_best[-1]
        # skip index 0 in r2l since we need at least two prices to make a pair
        r2l_best = 0
        for j in range(N - 1, 0, -1):
            r2l_max = max(prices[j], r2l_max)
            r2l_best = max(r2l_best, r2l_max - prices[j])
            retval = max(l2r_best[j - 1] + r2l_best, retval)
        return retval


class Solution:
    # no. 188
    # similar to above but using the idea of adjusting cost basis
    # essentially for an additional buy/sell pair, we can look at the profit of
    # buy/sell pairs without adding the new pair, and use the current price - previous profit
    # as the cost basis for new pair starting at the current price, the rest
    # is the same as if we are only buy/sell a single pair
    def maxProfit(self, k: int, prices: List[int]) -> int:
        buy_sells = k * [float("inf"), 0]

        for p in prices:
            for ki in range(k):
                buy_k = ki * 2
                sell_k = buy_k + 1
                if buy_k > 1:
                    prev_sell_k = buy_k - 1
                    new_buy_k_cost = p - buy_sells[prev_sell_k]
                else:
                    new_buy_k_cost = p
                buy_sells[buy_k] = min(new_buy_k_cost, buy_sells[buy_k])
                buy_sells[sell_k] = max(p - buy_sells[buy_k], buy_sells[sell_k])
        return buy_sells[-1]

    # no. 140
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        words = set(wordDict)
        n = len(s)
        retval = []

        def dfs(start_idx: int, curr_sequence: list):
            nonlocal retval
            for i in range(start_idx, n):
                if (word := s[start_idx : i + 1]) in words:
                    if i + 1 == n:
                        retval.append(" ".join(curr_sequence + [word]))
                    else:
                        dfs(i + 1, curr_sequence + [word])
            return

        dfs(0, [])
        return retval


if __name__ == "__main__":
    print(Solution().maxProfit(2, [3, 2, 6, 5, 0, 3]))
    print(Solution().wordBreak("catsanddog", ["cat", "cats", "and", "sand", "dog"]))
