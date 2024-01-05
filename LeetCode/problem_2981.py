"""
Difficulty: Normal

Topic: Find Longest Special Substring That Occurs Thrice I

Summary:
You are given a string s that consists of lowercase English letters.

A string is called special if it is made up of only a single character. For example, the string "abc" is not special, whereas the strings "ddd", "zz", and "f" are special.

Return the length of the longest special substring of s which occurs at least thrice, or -1 if no special substring occurs at least thrice.

A substring is a contiguous non-empty sequence of characters within a string.
"""
from collections import defaultdict

class Solution:
    def maximumLength(self, s: str) -> int:
        mps = defaultdict(int)
        count = 0
        for i in range(len(s)):
            count = 1
            mps[(s[i], count)] += 1
            for j in range(i, len(s)):
                if j + 1 < len(s) and s[j] == s[j + 1]:
                    count += 1
                    mps[(s[i], count)] += 1
                else:
                    break
        ans = 0
        for key, value in mps.items():
            if value >= 3:
                ans = max(ans, key[1])
        return ans if ans != 0 else -1
    
if __name__ == "__main__":
    solution = Solution()
    print(solution.maximumLength(s="aaaa"))