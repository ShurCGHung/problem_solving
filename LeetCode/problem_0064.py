"""
Difficulty: Medium

Topic: Minimum Path Sum

Summary:
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.
"""
from typing import List

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0

        rows = len(grid)
        cols = len(grid[0])

        dp = [[0] * cols for _ in range(rows)]

        dp[0][0] = grid[0][0]

        for i in range(1, cols):
            dp[0][i] = dp[0][i - 1] + grid[0][i]

        for i in range(1, rows):
            dp[i][0] = dp[i - 1][0] + grid[i][0]

        for i in range(1, rows):
            for j in range(1, cols):
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]
        
        return dp[rows - 1][cols - 1]

if __name__ == "__main__":
    solution = Solution()
    print(solution.minPathSum(grid=[
        [1, 3, 1],
        [1, 5, 1],
        [4, 2, 1]
    ]))