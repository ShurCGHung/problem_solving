"""
Category: Dynamic Programming
Difficulty: Easy

Question: Counting number of bit 1 of n + 1 numbers => return a list
"""
from typing import List
import time

class Solution:
    # Original Solution
    def countBits(self, n: int) -> List[int]:
        lst = []

        for i in range(n + 1):
            lst.append(bin(i)[2:].count('1'))

        return lst

    # Optimized Solution
    def countingBitsOne(self, number: int) -> List[int]:
        n_bits = [0] * (number + 1)

        for i in range(1, number + 1):
            n_bits[i] = n_bits[i >> 1] + (i & 1)

        return n_bits
    
if __name__ == "__main__":
    solution = Solution()
    start_time = time.time()
    print(solution.countingBitsOne(number=5))
    print(" --- %.10f seconds --- " % (time.time() - start_time))

    # start_time = time.time()
    # print(solution.countBits(n=5))
    # print(" --- %.10f seconds --- " % (time.time() - start_time))