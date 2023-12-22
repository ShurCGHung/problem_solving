"""
Difficulty: Medium

Question: Count Subarrays Where Max Element Appears at Least K Times
"""
from typing import List
from collections import deque

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        result = 0
        count = 0
        max_count = 0
        max_num = nums[0]

        for num in nums:
            max_num = max(max_num, num)
            if num == max_num:
                max_count += 1
                count = 0
            else:
                count += 1
                if count >= k:
                    result += max_count

        return result


if __name__ == "__main__":
    solution = Solution()
    nums = [61,23,38,23,56,40,82,56,82,82,82,70,8,69,8,7,19,14,58,42,82,10,82,78,15,82]
    k = 2
    print(solution.countSubarrays(nums=nums,k=k))