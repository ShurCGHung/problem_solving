"""
Difficult: Normal

Question: Double Modular Exponentiation
"""
from typing import List

class Solution:
    def getGoodIndices(self, variables: List[List[int]], target: int) -> List[int]:
        good_indices = []
        for indice in range(0, len(variables)):
            if (variables[indice][0] ** variables[indice][1] % 10) ** variables[indice][2] % variables[indice][3] == target:
                good_indices.append(indice)
        return good_indices
    
if __name__ == "__main__":
    solution = Solution()
    lst = [[2,3,3,10],[3,3,3,1],[6,1,1,4]]
    target = 2
    print(solution.getGoodIndices(variables=lst, target=target))