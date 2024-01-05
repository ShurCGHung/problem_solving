"""
Difficulty: Medium

Topic: Minimum Number of Operations to Make Array Empty

Summary: 
You are given a 0-indexed array nums consisting of positive integers.

There are two types of operations that you can apply on the array any number of times:

Choose two elements with equal values and delete them from the array.
Choose three elements with equal values and delete them from the array.
Return the minimum number of operations required to make the array empty, or -1 if it is not possible.
"""
from typing import List
from collections import Counter

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        mp = Counter(nums)
        count = 0
        for time in mp.values():
            if time == 1:
                return -1
            count += time // 3
            if time % 3:
                count += 1
        return count
    
if __name__ == "__main__":
    solution = Solution()
    solution.minOperations(nums=[2,3,3,2,2,4,2,3,4])