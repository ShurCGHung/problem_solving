"""
String to integer
"""
from typing import List
import time

class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()  # Remove leading and trailing spaces
        if not s:
            return 0
        
        sign = 1
        result = 0
        i = 0

        if (s[0] == '-'):
            sign = -1
            i += 1
        elif (s[0] == "+"):
            i += 1
        
        while i < len(s) and s[i].isdigit():
            result = result * 10 + int(s[i])
            i += 1
            if sign == 1 and result >= 2 ** 31 - 1:
                return 2 ** 31 - 1
            elif sign == -1 and result >= 2 ** 31:
                return -2 ** 31
            
        return sign * result
    
    def printMyList(self, s: str) -> List:
        lst = [string for string in s.split(' ')]
        print(lst)
        
        for each in lst:
            print(each)

if __name__ == "__main__":
    solution = Solution()
    start_time = time.time()
    print(solution.myAtoi(" with word -4193 "))
    print(" --- %.10f seconds --- " % (time.time() - start_time))