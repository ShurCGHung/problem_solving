"""
Difficulty: Easy

Question: Count tested devices after test operations
"""
from typing import List

class Solution:
    def countTestedDevices(self, batteryPercentages: List[int]) -> int:
        tested = 0
        
        for i in range(0, len(batteryPercentages)):
            if (batteryPercentages[i] > 0):
                tested += 1
                
                for j in range(i + 1, len(batteryPercentages)):
                    batteryPercentages[j] = max(0, batteryPercentages[j] - 1)
            
        return tested
    
if __name__ == "__main__":
    solution = Solution()
    print(solution.countTestedDevices(batteryPercentages=[1, 1, 2, 1, 3]))