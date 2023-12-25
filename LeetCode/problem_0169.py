"""
Difficulty: Easy

Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array
"""
from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = {}
        for num in nums:
            if num in counter:
                counter[num] += 1
            else:
                counter[num] = 1
        for key, value in counter.items():
            if value >= len(nums) / 2:
                return key