# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        current = dummy
        carry = 0

        while l1 or l2 or carry:
            sum_val = carry
            if l1:
                sum_val += l1.val
                l1 = l1.next
            if l2:
                sum_val += l2.val
                l2 = l2.next
            
            carry, val = divmod(sum_val, 10)
            current.next = ListNode(val)
            current = current.next
        
        return dummy.next
    
def display_linked_list(node):
    while node:
        print(node.val, end=" -> " if node.next else "\n")
        node = node.next

if __name__ == "__main__":
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)

    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)
    
    solution = Solution()
    result = solution.addTwoNumbers(l1, l2)

    print("Input:")
    display_linked_list(l1)
    display_linked_list(l2)
    print("Output:")
    display_linked_list(result)