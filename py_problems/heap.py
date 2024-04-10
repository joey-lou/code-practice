from heapq import heappop, heappush
from typing import List


class Solution:
    def findMaximizedCapital(
        self, k: int, w: int, profits: List[int], capital: List[int]
    ) -> int:
        n = len(profits)
        heap = []
        projects = sorted(zip(capital, profits), key=lambda x: x[0])
        i = 0
        for _ in range(k):
            while i < n and projects[i][0] <= w:
                heappush(heap, -projects[i][1])
                i += 1
            if heap:
                w -= heappop(heap)
        return w


class Solution:
    def kSmallestPairs(
        self, nums1: List[int], nums2: List[int], k: int
    ) -> List[List[int]]:
        # think of it as a matrix, and we are expanding the frontier
        retval = []
        m, n = len(nums1), len(nums2)

        if not m or not n:
            return retval
        seen = set()
        heap = [(nums1[0] + nums2[0], 0, 0)]
        while k and heap:
            _, i, j = heappop(heap)
            if (i, j) in seen:
                continue
            seen.add((i, j))
            retval.append([nums1[i], nums2[j]])
            k -= 1

            if i < m - 1:
                heappush(heap, (nums1[i + 1] + nums2[j], i + 1, j))

            if j < n - 1:
                heappush(heap, (nums1[i] + nums2[j + 1], i, j + 1))

            if i < m - 1 and j < n - 1:
                heappush(heap, (nums1[i + 1] + nums2[j + 1], i + 1, j + 1))

        return retval


if __name__ == "__main__":
    print(Solution().kSmallestPairs([1, 1, 2], [2, 4, 6], 15))
