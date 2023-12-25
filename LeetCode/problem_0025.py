"""
Difficulty: Hard

The problem statement for LeetCode Problem 25 is to reverse the nodes of a linked list k at a time and return its head
"""
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        groupPrev = dummy
        while True:
            kth = self.getKth(groupPrev, k=k)
            if not kth:
                break
            groupNext = kth.next
            prev, curr = kth.next, groupPrev.next
            while curr != groupNext:
                nextNode = curr.next
                curr.next = prev
                prev = curr
                curr = nextNode
            nextGroupPrev = groupPrev.next
            groupPrev.next = prev
            groupPrev = nextGroupPrev
        return dummy.next       

    def getKth(self, curr: Optional[ListNode], k: int) -> Optional[ListNode]:
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr
    
if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)

    kGroup = 2

    lst = Solution().reverseKGroup(head=head, k=kGroup)

    while lst:
        if lst.next is not None:
            print(f"{lst.val} ->", end=" ")
        else:
            print(lst.val)
        lst = lst.next