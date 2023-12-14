"""
Category
Difficulty: Medium

K Divisible elements subarray
"""
import time
from typing import List

class Solution:
    def countDistinct(self, nums: List[int], k: int, p: int) -> int:
        lst = set()

        for start in range(len(nums)):
            count = 0
            temp = ''
            for i in range(start, len(nums)):
                if nums[i] % p == 0:
                    count += 1
                temp += str(nums[i]) + ','
                if count > k:
                    break
                lst.add(temp)

        return len(lst)

if __name__ == "__main__":
    solution = Solution()
    start_time = time.time()
    print(solution.countDistinct(nums=[2, 3, 3, 2, 2], k=2, p=2))
    print(" --- %.10f seconds --- " % (time.time() - start_time))