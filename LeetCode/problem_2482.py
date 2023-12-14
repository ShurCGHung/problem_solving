"""
Difference Between Ones and Zeros in Row and Column
"""
from typing import List

class Solution:
    def countOneOnRow(self, grid: List[List[int]], row: int) -> int:
        return sum(1 for i in grid[row] if i == 1)

    def countOneOnCol(self, grid: List[List[int]], col: int) -> int:
        return sum(1 for row in grid if row[col] == 1)

    def countZeroOnRow(self, grid: List[List[int]], row: int) -> int:
        return sum(1 for i in grid[row] if i == 0)

    def countZeroOnCol(self, grid: List[List[int]], col: int) -> int:
        return sum(1 for row in grid if row[col] == 0)

    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        rows = len(grid)
        cols = len(grid[0])

        # Initialize diff list with zeros of the same dimensions as the grid
        diff = [[0 for _ in range(cols)] for _ in range(rows)]

        for i in range(rows):
            for j in range(cols):
                diff[i][j] = self.countOneOnRow(grid, i) + self.countOneOnCol(grid, j) - self.countZeroOnRow(grid, i) - self.countZeroOnCol(grid, j)

        return diff
    

if __name__ == "__main__":
    solution = Solution()

    grid = [
        [0,1,1],
        [1,0,1],
        [0,0,1]
        ]

    print(solution.onesMinusZeros(grid=grid))