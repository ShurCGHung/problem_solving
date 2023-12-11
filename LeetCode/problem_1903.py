# You are given a string num, representing a large integer. Return the largest-valued odd integer (as a string) that is a non-empty substring of num, 
# or an empty string "" if no odd integer exists.

# A substring is a contiguous sequence of characters within a string.

class Solution:
    def largestOddNumber(self, num: str) -> str:
        # Starting from the end of the string
        for i in range(len(num) - 1, -1, -1):
            digit = int(num[i])
            # Check if the digit is odd
            if digit % 2 != 0:
                # Return the largest odd substring from the beginning to this digit
                return num[:i + 1]
        # If no odd number found, return an empty string
        return ""