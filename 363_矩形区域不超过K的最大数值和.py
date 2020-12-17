from typing import List

class Solution1:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        rows, cols = len(matrix), len(matrix[0])
        res = float('-inf')
        for row1 in range(1, rows + 1):
            for col1 in range(1, cols + 1):
                dp = [[0 for i in range(cols + 1)] for j in range(rows + 1)]
                dp[row1][col1] = matrix[row1 - 1][col1 - 1]
                for row2 in range(row1, rows + 1):
                    for col2 in range(col1, cols + 1):
                        dp[row2][col2] = dp[row2][col2 - 1] + dp[row2 - 1][col2]\
                                         - dp[row2 - 1][col2 - 1] + matrix[row2 - 1][col2 - 1]
                        if dp[row2][col2] > res and dp[row2][col2] <= k:
                            res = dp[row2][col2]
        return res


import bisect
class Solution2:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int :
        row, col = len(matrix), len(matrix[0])
        res = float('-inf')
        for left in range(col):
            _sum = [0] * row
            for right in range(left, col):
                for i in range(row):
                    _sum[i] += matrix[i][right]
                arr, cur = [0], 0
                for tmp in _sum:
                    cur += tmp
                    loc = bisect.bisect_left(arr, cur - k)
                    if loc < len(arr):
                        res = max(cur - arr[loc], res)
                    bisect.insort(arr, cur)
        return res