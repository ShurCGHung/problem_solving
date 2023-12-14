"""
Difficulty: Medium

Question: Reverse integer
"""
import time

class Solution:
    def reverse(self, x: int) -> int:
        sign = 1

        if (x < 0):
            sign = -1
            x *= -1
        else:
            sign = 1

        new_number = 0

        while (x > 0):
            new_number = new_number * 10 + x % 10
            x //= 10
        
        result = new_number * sign
        
        if result > 2 ** 31 - 1 or result < - 2 ** 31:
            return 0
        
        return result
    
if __name__ == "__main__":
    solution = Solution()
    start_time = time.time()
    print(solution.reverse(123))
    print(" --- %.10f seconds --- " % (time.time() - start_time))