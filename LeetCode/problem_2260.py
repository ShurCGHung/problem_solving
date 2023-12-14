"""
Difficulty: Medium

Minimum Consecutive Cards to pick up
"""
from typing import List
import time

class Solution:
    # Original solution
    def minimumCardPickup(self, cards: List[int]) -> int:
        min_vals = []
        
        for i in range(len(cards) - 1):
            count = 1
            for j in range(i + 1, len(cards)):
                count += 1
                if (cards[i] == cards[j]):
                    min_vals.append(count)

        return min(min_vals) if min_vals else -1

    # Optimized solution
    # def minimumCardPickup(self, cards: List[int]) -> int:
    #     indices = {}
    #     min_diff = float('inf')
        
    #     for i, card in enumerate(cards):
    #         if card in indices:
    #             min_diff = min(min_diff, i - indices[card] + 1)
    #         indices[card] = i
                
    #     return min_diff if min_diff != float('inf') else -1

if __name__ == "__main__":
    solution = Solution()

    lst_cards = [3,4,2,3,4,7]
    start_time = time.time()
    print(solution.minimumCardPickup(cards=lst_cards))
    print(" --- %.10f seconds --- " % (time.time() - start_time))