# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None: return
        prev = head 
        curr = head.next
        next = None
        while head is not None:
            prev.next = None
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return head
    
Solution.reverseList(head=[1,2,3,4,5])
