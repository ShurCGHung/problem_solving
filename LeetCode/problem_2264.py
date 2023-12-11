"""
You are given a string num representing a large integer. An integer is good if it meets the following conditions:

It is a substring of num with length 3.
It consists of only one unique digit.
Return the maximum good integer as a string or an empty string "" if no such integer exists.

Note:

A substring is a contiguous sequence of characters within a string.
There may be leading zeroes in num or a good integer.
"""

class Solution:
    def are_all_characters_same(self, s) -> bool:
        if not s:
            return False  # Return False for an empty string
        first_char = s[0]
        for char in s[1:]:
            if char != first_char:
                return False
        return True

    def largestGoodInteger(self, num: str) -> str:
        lst = []

        for index in range(0, len(num) - 2):
            substring = num[index:(index + 3)]
            
            if self.are_all_characters_same(substring) and (substring[0] != '0' or substring == "000"):
                lst.append(substring)

        if not lst:
            return ""
        else:
            max_val = max(lst)  # Find the maximum string among valid substrings
            return max_val

solution = Solution()
val = solution.largestGoodInteger("6777133339")
print(val)

# Shorter solution
"""
class Solution:
    def largestGoodInteger(self, num: str) -> str:
        max_val = ""
        for i in range(len(num) - 2):
            if num[i] == num[i + 1] == num[i + 2]:
                if num[i] != '0' or num[i:i+3] == "000":
                    max_val = max(max_val, num[i:i + 3])

        return max_val
"""