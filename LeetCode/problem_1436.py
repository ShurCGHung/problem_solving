"""
Difficulty: Easy

Topic: Destination City
"""
from typing import List

class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        source = set()
        destination = set()
        for path in paths:
            source.add(path[0])
            destination.add(path[1])
        for city in destination:
            if city not in source:
                return city
        return ""
    
if __name__ == "__main__":
    solution = Solution()

    city_paths = [["London", "New York"], ["New York", "Lima"], ["Lima", "Sao Paulo"]]

    print(solution.destCity(paths=city_paths))