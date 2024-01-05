"""
Difficulty: Easy

Topic: Minimum Operations to Collect Elements

Summary:
You are given an array nums of positive integers and an integer k.

In one operation, you can remove the last element of the array and add it to your collection.

Return the minimum number of operations needed to collect elements 1, 2, ..., k.
"""
from typing import List

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        operations = 0
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] <= k:
                operations |= 1 << (nums[i] - 1) # Mark if the number is less than or equal to k
            if operations == (1 << k) - 1: # If all numbers from 1 to k are marked
                return len(nums) - i
        return -1
    
    def minOperations2(self, nums: List[int], k: int) -> int:
        c = set()
        operations = 0
        while True:
            if nums[-1] <= k:
                c.add(nums.pop())
            else:
                nums.pop()
            operations += 1
            if len(c) == k:
                return operations
    
if __name__ == "__main__":
    solution = Solution()
    print(solution.minOperations(nums=[3, 1, 5, 4, 2], k=4))