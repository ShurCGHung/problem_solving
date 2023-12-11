"""
You are given an array of strings words and a string chars.

A string is good if it can be formed by characters from chars (each character can only be used once).

Return the sum of lengths of all good strings in words.
"""

from collections import Counter
from typing import List

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        char_count = Counter(chars)
        exist = []

        for word in words:
            word_count = Counter(word)
            can_form = True

            for (char, count) in word_count.items():
                if char_count[char] < count:
                    can_form = False
                    break

            if can_form:
                exist.append(word)

        total = 0

        for each in exist:
            total += len(each)

        return total

solution = Solution()
words = ["cat","bt","hat","tree"]
chars = "atach"
result = solution.countCharacters(words, chars)
print(result)