"""
Longest Palindrome substring
"""
import time

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 2 or s == s[::-1]:
            return s

        start, max_len = 0, 0

        for i in range(len(s)):
            len1 = self.expand_around_center(s, i, i)  # Odd length palindrome
            len2 = self.expand_around_center(s, i, i + 1)  # Even length palindrome
            length = max(len1, len2)

            if length > max_len:
                max_len = length
                start = i - (length - 1) // 2

        return s[start:start + max_len]

    def expand_around_center(self, s: str, left: int, right: int) -> int:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        
        return right - left - 1

if __name__ == "__main__":
    start_time = time.time()
    solution = Solution()
    print(solution.longestPalindrome("babad"))
    print(" --- %.10f seconds --- " % (time.time() - start_time))