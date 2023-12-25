"""
Difficulty: Medium

Topic: Combination Sum

Summary:
Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the 
frequency of at least one of the chosen numbers is different.

The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.
"""
from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(start, path, target):
            if target < 0:
                return
            if target == 0:
                result.append(path)
                return

            for i in range(start, len(candidates)):
                backtrack(i, path + [candidates[i]], target - candidates[i])

        result = []
        candidates.sort()
        backtrack(0, [], target)
        return result
    
if __name__ == "__main__":
    sol = Solution()
    candidates = [2, 3, 6, 7]
    target = 7
    result = sol.combinationSum(candidates, target)
    print(result)