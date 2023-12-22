"""
Category:
Difficulty: Medium

Question sum of triplets result to 0
- No duplicate
- Order of the triplet does not matter
"""
from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # Sort the input list

        result = []
        n = len(nums)

        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue  # Skip duplicates in the first position of the triplet

            left, right = i + 1, n - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    result.append([nums[i], nums[left], nums[right]])

                    # Skip duplicates in the second position of the triplet
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    # Skip duplicates in the third position of the triplet
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1

        return result
    
if __name__ == "__main__":
    solution = Solution()
    print(solution.threeSum(nums=[-1, 0, 1, 2, -1, -4]))