from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        stack = [(list(), nums)]
        while stack:
            current, remaining = stack.pop()
            if len(current) == len(nums):
                result.append(current)
            else:
                for i in range(len(remaining)):
                    stack.append((current + [remaining[i]], remaining[:i] + remaining[i + 1:]))
        return result
    
if __name__ == "__main__":
    solution = Solution()
    lst = solution.permute(nums=[1, 2, 3])
    for each in lst:
        print(each)