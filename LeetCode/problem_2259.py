"""
Difficulty: Easy

Remove Digit From Number to Maximize Result
"""
import time

class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        lst = []

        for i in range(len(number)):
            if number[i] == digit:
                lst.append(int(number[:i] + number[i + 1:]))
        
        return str(max(lst))


if __name__ == "__main__":
    string = "1231"
    digit = "1"
    solution = Solution()
    start_time = time.time()
    print(solution.removeDigit(number=string, digit=digit))
    print(" --- %.10f seconds --- " % (time.time() - start_time))