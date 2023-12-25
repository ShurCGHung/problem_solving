"""
Difficulty: Medium

Given the head of a linked list, remove the nth node from the end of the list and return its head
"""
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # slow and fast node, point at the head
        slow = fast = head
        for _ in range(n): # Move fast pointer n step ahead
            fast = fast.next
        if not fast: # if None, remove head from the list
            return head.next
        # Move both slow and fast one step unless fast.next is null
        while fast.next:
            slow = slow.next
            fast = fast.next
        # Skip the next node of slow
        slow.next = slow.next.next
        return head
    
if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)

    solution = Solution()
    result = solution.removeNthFromEnd(head=head, n=2)
    
    while result:
        if result.next is not None:
            print(f"{result.val} ->", end=" ")
        else:
            print(result.val)
        result = result.next