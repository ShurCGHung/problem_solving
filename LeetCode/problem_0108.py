"""
Difficulty: Easy

Topic: Convert Sorted Array to Binary Search Tree


Summary:
Given an integer array nums where the elements are sorted in ascending order, convert it to a 
height-balanced binary search tree.
"""
from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        
        def helper(left, right):
            if left > right:
                return None
        
            mid = (left + right) // 2
            root = TreeNode(nums[mid])
            root.left = helper(left, mid - 1)
            root.right = helper(mid + 1, right)
            return root
        
        return helper(0, len(nums) - 1)
    
if __name__ == "__main__":
    solution = Solution()
    print(solution.sortedArrayToBST(nums=[-10, -3, 0, 5, 9]))