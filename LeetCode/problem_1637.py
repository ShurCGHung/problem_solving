from typing import List

class Solution:
    def printSortedPoints(self, points: List[List[int]]) -> List[List[int]]:
        points.sort(key = lambda x: x[0])
        return points

    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[0])
        max_width = 0
        
        # Calculate the maximum width without points in between
        for i in range(1, len(points)):
            width = points[i][0] - points[i - 1][0]
            max_width = max(max_width, width)
        
        return max_width

if __name__ == "__main__":
    solution = Solution()   
    points=[[3,1],[9,0],[1,0],[1,4],[5,3],[8,8]]
    print(solution.maxWidthOfVerticalArea(points=points))