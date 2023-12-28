"""
Difficulty: Medium

Topics: Minimum Time to Make Rope Colorful

Summary: Alice has n balloons arranged on a rope. You are given a 0-indexed string colors where colors[i] is the color of the ith balloon.

Alice wants the rope to be colorful. She does not want two consecutive balloons to be of the same color, so she asks Bob for help. Bob can remove some balloons from the rope to make it colorful. You are given a 0-indexed integer array neededTime where neededTime[i] is the time (in seconds) that Bob needs to remove the ith balloon from the rope.

Return the minimum time Bob needs to make the rope colorful.
"""
from typing import List

class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        result_score = max_score = total_cost  = 0
        for i in range(len(colors)):
            if i > 0 and colors[i] != colors[i - 1]:
                result_score += total_cost - max_score
                max_score = total_cost = 0
            total_cost += neededTime[i]
            max_score = max(max_score, neededTime[i])
        result_score += total_cost - max_score
        return result_score
    
if __name__ == "__main__":
    solution = Solution()
    print(solution.minCost(colors="aabaa", neededTime=[1,2,3,4,1]))
