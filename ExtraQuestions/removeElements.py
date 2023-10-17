# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        # input: a listnode, val
        # output: listnode with nodes correspending to val removed

        # iterate down the list and remove listnodes corresponding to val
        # keep a pointer on the last node.val != val, point to the next node with node.val != val
        curr = head
        lastValid = None
        newHead = None
        while curr != None:
            if curr.val != val:
                if lastValid:
                    lastValid.next = curr
                    lastValid = curr
                else:
                    lastValid = curr
                    newHead = curr
            curr = curr.next

        # trim the end
        if lastValid:
            lastValid.next = None

        return newHead

# [7,6,7,6] val = 7
#  ^
#
