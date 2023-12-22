"""
Difficulty: Medium

Question: Letter Combinations of a Phone Number
"""
from typing import List
import time

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        mapping = {
            "0": [],
            "1": [],
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "r", "q", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }
        def backtrack(combination, next_digits):
            if not next_digits:
                output.append(combination)
            else:
                for letter in mapping[next_digits[0]]:
                    backtrack(combination + letter, next_digits[1:])
        output = []
        backtrack("", digits)
        return output, len(output)
    
if __name__ == "__main__":
    solution = Solution()
    start_time = time.time()
    print(solution.letterCombinations(digits='77874446'))
    print(" --- %.10f seconds --- " % (time.time() - start_time))