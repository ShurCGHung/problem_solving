"""
Difference Between Ones and Zeros in Row and Column
"""
from typing import List

class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        rows = len(grid)
        cols = len(grid[0])

        row_ones = [0] * rows
        col_ones = [0] * cols
        row_zeros = [0] * rows
        col_zeros = [0] * cols
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    row_ones[i] += 1
                    col_ones[j] += 1
                else:
                    row_zeros[i] += 1
                    col_zeros[j] += 1

        diff = [[0] * cols for _ in range(rows)]

        for i in range(rows):
            for j in range(cols):
                diff[i][j] = row_ones[i] + col_ones[j] - row_zeros[i] - col_zeros[j]

        return diff
    
if __name__ == "__main__":
    solution = Solution()

    grid = [
        [0,1,1],
        [1,0,1],
        [0,0,1]
        ]

    print(solution.onesMinusZeros(grid=grid))